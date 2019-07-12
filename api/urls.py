from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^v1/project_types$', views.ProjectTypeList.as_view(),
        name='project_type_list'),  # 获取项目类型
    url(r'^v1/projects$', views.ProjectList.as_view(),
        name='project_list'),  # 获取项目列表
    url(r'^v1/process$', views.ProcessMit.as_view()),  # 监控进程是否存在
    url(r'^v1/project/(?P<id>\d+)$', views.ProjectDetail.as_view()),  # 项目详情
    url(r'^v1/db$', views.Database.as_view()),  # 项目详情
    url(r'^v1/options$', views.OptionView.as_view()),  # 待选选项
    url(r'^v1/draft$', views.DraftView.as_view()),  # 测试接口
    # url(r'^v3/results/(?P<pk>\d+)$',
    #     views.ResultDetail.as_view(), name='result_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
