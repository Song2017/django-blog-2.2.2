from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('hello django')


def hellot(request):
    context = {}
    context['hello'] = 'hello from template'
    context['athlete_list'] = ['ath_jack', 'smith', 'cuinidy', 'neo']
    context['user'] = 'song'
    context['currentuser'] = 'song2'
    return render(request, 'hello.html', context=context)
