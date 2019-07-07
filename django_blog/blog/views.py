from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(
        req,
        "blog/index.html",
        context={"title": "Blog Home", "welcome": "Here is Blog Home Page"},
    )

