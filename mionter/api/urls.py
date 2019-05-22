from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^v3/project_types', views.ProjectTypeList.as_view(),
        name='project_type_list'),
    # url(r'^v3/results/(?P<pk>\d+)$',
    #     views.ResultDetail.as_view(), name='result_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
