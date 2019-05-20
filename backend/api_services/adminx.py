import xadmin

from xadmin import views
from django.conf import settings
from .models import Project, ProjectType


# 主题设置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 全局设置
class GlobalSetting(object):
    site_title = '智能采集平台后台管理'
    site_footer = '个人测试'
    menu_style = 'accordion'  # 折叠菜单


# 定制设置
class LabelSetting(object):
    show_bookmarks = False
    list_per_page = 100


class ProjectAdmin(LabelSetting):
    search_fields = ('name',)
    list_display = ['name', 'type', 'users', 'created_at', 'updated_at']
    list_filter = ['name', 'created_at', 'updated_at']
    list_export = ['csv', 'json']
    filter_horizontal = (settings.AUTH_USER_MODEL, )
    style_fields = {'users': 'm2m_transfer', }


class ProjectTypeAdmin(LabelSetting):
    search_fields = ('name',)
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['name', 'created_at', 'updated_at']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(ProjectType, ProjectTypeAdmin)
xadmin.site.register(Project, ProjectAdmin)
