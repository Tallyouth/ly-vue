from label.serializers import VerifyJSONWebTokenSerializer
from django.forms import ValidationError
from django.contrib.auth.models import User


def getUserFromToken(token):
    data = {'token': token}
    try:
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        username = valid_data['user']
    except ValidationError as v:
        print("validation error", v)
    return User.objects.filter(username=username).first()
