from api.models import ProjectType, Project
from api.serializers import ProjectTypeSerializer, ProjectSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from utils.mionter import judgeprocess
from utils.database import Mongodb


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
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProjectTypeList(generics.ListAPIView):
    serializer_class = ProjectTypeSerializer
    queryset = ProjectType.objects.all()


class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    pagination_class = CustomPageNumberPagination

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


# 获取爬虫数据
class Database(APIView):
    def get(self, request):
        try:
            dbconfig = {
                'host': '192.168.1.184',
                'port': 27017,
                'user': '',
                'password': '',
            }
            with Mongodb(dbconfig) as db:
                data = db.database_info()
            return OkResponse(data=data)
        except Exception as e:
            return FailResponse(msg=str(e))


# 待选选项
class OptionView(APIView):
    def get(self, request):
        try:
            data = Project.objects.filter(dbname__isnull=False).values('name', 'dbname')
            newarry = []
            for i in data:
                dic = {}
                dic["value"] = i["dbname"]
                dic["label"] = i["name"]
                newarry.append(dic)
            return OkResponse(data=newarry)
        except Exception as e:
            return FailResponse(msg=str(e))


# 修改期刊数据接口
class DraftView(APIView):
    def post(self, request):
        try:
            dbconfig = {
                'host': '192.168.1.184',
                'port': 27017,
                'user': '',
                'password': '',
                'database': 'journal'
            }
            collection_name = 'issn_info'
            data = request.data
            with Mongodb(dbconfig) as mongo:
                query = {'series_id': data['series_id']}
                form = {'$set': data['data']}
                mongo.update_one(collection_name, query, form)
                result = mongo.find_one(collection_name, query)
            return OkResponse(data=result)
        except Exception as e:
            return FailResponse(msg=str(e))
