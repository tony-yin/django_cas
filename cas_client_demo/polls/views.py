# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required  
 
@login_required  
def index(request):
    return HttpResponse("176: 你好，欢迎来到投票系统的主页")
