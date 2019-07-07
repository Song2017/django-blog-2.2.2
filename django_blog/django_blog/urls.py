"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.template import loader, RequestContext


def index(request):
    print(request, type(request))

    # tpl = loader.get_template('index.html')
    # context = {'content': 'www.test.com', 'user': 'user1'}
    # return HttpResponse(tpl.render(context))
    # 模板: 大字符串填空, 不适合异步
    # return render(request, 'index.html', {
    #     'content': 'www.test.com',
    #     'user': 'user1'
    # })

    return render(request, 'index.html',
                  {'nums': dict(zip('abcdef', range(6)))})
    # return JsonResponse({'name': 'hello blog'})  # ttpResponse('hello blog')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index$', index),
    url(r'^$', include('blog.urls')),

    url(r'^user/', include('user.urls')),
]
