# -*- coding: utf-8 -*-
# @Author: 三木
# @Date:   2018-10-20 22:06:55
# @Last Modified by:   三木
# @Last Modified time: 2018-10-22 16:00:46
from django.conf.urls import url
from . import views

app_name='blog'  

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
]