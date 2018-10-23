# -*- coding: utf-8 -*-
# @Author: 三木
# @Date:   2018-10-22 14:11:14
# @Last Modified by:   三木
# @Last Modified time: 2018-10-22 14:36:56
from django import template
from ..models import Post,Category

register=template.Library()     #实例化template.Library()类

@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
	return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
	return Category.objects.all()
	