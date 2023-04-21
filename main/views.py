from django.shortcuts import render


# Create your views here.


def hello(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')