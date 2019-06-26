from api.models import ProjectType, Project
from api.serializers import ProjectTypeSerializer, ProjectSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from utils.mionter import judgeprocess


class OkResponse(Response):
    def __init__(self, data=None, **kwargs):
        _data = {}
        if data:
            _data['data'] = data
        _data['code'] = 200
        _data['msg'] = 'success'
        super().__init__(_data, **kwargs)


class FailResponse(Response):
    def __init__(self, data=None, code=40000, msg='fail', **kwargs):
        _data = {}
        if data:
            _data['data'] = data
        _data['code'] = code
        _data['msg'] = msg
        super().__init__(_data, **kwargs)


class ProcessMit(APIView):
    def post(self, request):
        try:
            processname = request.data['processname']
            if judgeprocess(processname):
                return OkResponse(data={"statu": 1})
            else:
                return OkResponse(data={"statu": 0})
        except Exception as e:
            return FailResponse(msg=str(e))


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProjectTypeList(generics.ListAPIView):
    serializer_class = ProjectTypeSerializer
    queryset = ProjectType.objects.all()


class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        type_id = self.request.query_params.get('type_id')
        return Project.objects.filter(type=type_id)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    # queryset = Project.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['id'])

    def update(self, request, *args, **kwargs):
        project = self.get_object()
        project.desc = request.data['desc']
        project.name = request.data['name']
        project.save()
        serializer = self.get_serializer(project)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            project = self.get_object()
            project.delete()
            return OkResponse()
        except Exception as e:
            return FailResponse(msg=str(e))
