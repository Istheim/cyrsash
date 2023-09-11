from django.shortcuts import render


def base(request):
    return render(request, 'dispatches/base.html')


def home(request):
    return render(request, 'dispatches/home.html')
