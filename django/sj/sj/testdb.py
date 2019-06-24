# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
    test1 = Test(name='dajiao')
    test1.save()
    return HttpResponse('数据添加成功')


def dball(request):
    context = {}
    context['athlete_list'] = []
    rts = Test.objects.all()
    for i, var in enumerate(rts):
        context['athlete_list'].append((i, var.name))
    context['user'] = 'song'
    context['currentuser'] = 'song2'
    return render(request, 'hello.html', context=context)


def dbope(request):
    request.encoding = 'utf-8'
    paras = request.get_full_path().split('?')
    if paras[1] == 'update':
        r1 = Test.objects.get(id=int(paras[2]))
        r1.name = paras[3]
        r1.save()
        return dball(request)
    elif paras[1] == 'updateall':
        Test.objects.all().update(name=paras[2])
        return dball(request)
    elif paras[1] == 'del':
        r1 = Test.objects.get(id=int(paras[2]))
        r1.delete()
        return dball(request)
    elif paras[1] == 'delall':
        Test.objects.all().delete()
        return dball(request)
    elif paras[1] == 'add':
        test1 = Test(name=paras[2])
        test1.save()
        return dball(request)
    resp1 = ''
    r1 = Test.objects.filter(id=1)
    for var in r1:
        resp1 += ', ' + var.name
    resp2 = Test.objects.get(id=1)

    return HttpResponse('resp1 is ' + resp1 + ', resp2 is ' + resp2.name)
