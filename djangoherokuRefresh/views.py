from django.shortcuts import render


def home(request):
    return render(request, 'djangoherokurefresh/index.html')


def view(request):
    return render(request, 'djangoherokurefresh/views.html', {'name': request.GET.get('FirstName')})
