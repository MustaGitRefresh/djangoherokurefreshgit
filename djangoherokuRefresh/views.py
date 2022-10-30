from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'djangoherokurefresh/index.html')


def view(request):
    print(request.GET.get("FirstName"))
    return HttpResponse("done")
