# -*- coding: utf-8 -*-
# @Author: 三木
# @Date:   2018-10-22 20:33:21
# @Last Modified by:   三木
# @Last Modified time: 2018-10-22 20:36:42
from django.conf.urls import url

from . import views

app_name='comments'
urlpatterns=[
	url(r'^comment/post/(?P<post_pk>[0-9]+)/$',views.post_comment,name='post_comment'),
]