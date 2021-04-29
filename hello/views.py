from django.shortcuts import render
from django.http import HttpResponse
import requests,os
from .models import Greeting

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',default=3))
    return HttpResponse(content="Hello!" * times)
    # r = requests.get('http://httpbin.org/status/418')
    # return HttpResponse('<pre>' + r.text + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
