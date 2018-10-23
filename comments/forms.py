# -*- coding: utf-8 -*-
# @Author: 三木
# @Date:   2018-10-22 19:50:41
# @Last Modified by:   三木
# @Last Modified time: 2018-10-22 20:32:21
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['name','email','url','text']