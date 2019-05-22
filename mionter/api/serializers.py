import jwt

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import get_username_field, PasswordField
from api.models import Project, ProjectType

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class Serializer(serializers.Serializer):
    @property
    def object(self):
        return self.validated_data


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = "__all__"


class User_id(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')


class Project_id(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'type', 'created_at', 'updated_at')


class JSONWebTokenSerializer(Serializer):
    """
    Serializer class used to validate a username and password.
    'username' is identified by the custom UserModel.USERNAME_FIELD.
    Returns a JSON Web Token that can be used to authenticate later calls.
    """

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    @property
    def username_field(self):
        return get_username_field()

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


class VerificationBaseSerializer(Serializer):
    """
    Abstract serializer used for verifying and refreshing JWTs.
    """
    token = serializers.CharField()

    def validate(self, attrs):
        msg = 'Please define a validate method.'
        raise NotImplementedError(msg)

    def _check_payload(self, token):
        # Check payload valid (based off of JSONWebTokenAuthentication,
        # may want to refactor)
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise serializers.ValidationError(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise serializers.ValidationError(msg)

        return payload

    def _check_user(self, payload):
        username = jwt_get_username_from_payload(payload)

        if not username:
            msg = _('Invalid payload.')
            raise serializers.ValidationError(msg)

        # Make sure user exists
        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            msg = _("User doesn't exist.")
            raise serializers.ValidationError(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise serializers.ValidationError(msg)

        return user


class VerifyJSONWebTokenSerializer(VerificationBaseSerializer):
    """
    Check the veracity of an access token.
    """

    def validate(self, attrs):
        token = attrs['token']

        payload = self._check_payload(token=token)
        user = self._check_user(payload=payload)

        return {
            'token': token,
            'user': user
        }
