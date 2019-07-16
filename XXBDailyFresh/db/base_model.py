#!/usr/bin/python
# -*- coding: UTF-8 -*-

# file      :   base_model.py
# @Time     :   2019-07-13 23:22
# @Author   :   xiaobing5
# @Email    :   lhxiaobing@qq.com

from django.db import models


class BaseModel(models.Model):
    """
    模型抽象基类
    """
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="删除标记")

    class Meta:
        # 说明是一个抽象模型类(不声明得话，生成数据库迁移文件的时候会把这个类也给创建一个数据库)
        abstract = True
