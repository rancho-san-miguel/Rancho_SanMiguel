from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def index2(request):
    return render(request, 'home/index2.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contacto.html')

def blog(request):
    return render(request, 'home/blog.html')

def element(request):
    return render(request, 'home/element.html')

def portfolio(request):
    return render(request, 'home/portfolio.html')

def service(request):
    return render(request, 'home/service.html')