# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf


def search_post(request):
    request.encoding = 'utf-8'
    ctx = {}
    if request.POST:
        message = '搜索的内容是: ' + request.POST['q']
    else:
        message = '空表单'
    ctx["rlt"] = message
    return render(request, "search_post.html", context=ctx)
