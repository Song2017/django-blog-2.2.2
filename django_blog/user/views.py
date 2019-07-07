from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.http import HttpResponseBadRequest
import simplejson
import logging

from .models import User
from django.db.models.query import *


def checkemail(request):
    return HttpResponse()


# Create your views here.
def reg(request: HttpRequest):
    print(request.body, request.GET, request.POST)
    print(simplejson.loads(request.body.decode()))
    try:
        # get count first last exist
        qs = User.objects.all()[1:3]
        print('result set', qs.query)
        for u in qs:
            print('u:', u.name)
        qs = User.objects.get(pk=1)
        print('result set get', qs)
        # 字段查询表达式
        # exact contains startswith/endswith lt/gt in iexact(insensitive)
        qs = User.objects.filter(pk__lt=1)
        print('result set filter', qs.query, qs.model)

        userload = simplejson.loads(request.body)
        email = userload['email']
        print(userload['email'], userload['password'], userload['name'])
        qs = User.objects.filter(email=email)
        print('objects', qs, type(qs))
        # email exists
        if qs:
            return HttpResponseBadRequest('email exists')

        user = User()
        user.email = email
        user.name = userload['name']
        user.password = userload['password']
        try:
            user.save()
            return JsonResponse({'result': 'user {} reged'.format(user.name)})
        except Exception as e:
            return HttpResponse('reg failed')
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()
