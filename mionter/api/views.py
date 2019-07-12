from api.models import ProjectType
from api.serializers import ProjectTypeSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProjectTypeList(generics.ListAPIView):
    serializer_class = ProjectTypeSerializer
    queryset = ProjectType.objects.all()
