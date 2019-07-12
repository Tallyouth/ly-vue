from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings


class ProjectType(models.Model):
    """项目类型表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='类型名', max_length=100)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = '项目类型'
        verbose_name_plural = '项目类型'


class Project(models.Model):
    """项目表"""
    id = models.AutoField(primary_key=True)  # 自增主键
    name = models.CharField(verbose_name='项目名', max_length=100)  # 项目名
    dbname = models.CharField(verbose_name="表名称", max_length=1000, blank=True, null=True)
    type = models.ForeignKey(
        ProjectType,
        verbose_name='项目类别',
        on_delete=models.CASCADE)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='用户',
        blank=True,
    )
    desc = models.CharField(verbose_name="介绍", max_length=1000, blank=True, null=True)
    statu = models.CharField(verbose_name='状态', max_length=100)
    created_at = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True)  # 创建时间
    updated_at = models.DateTimeField(
        verbose_name='修改时间', auto_now=True)  # 修改时间

    class Meta:
        ordering = ('id',)
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name
