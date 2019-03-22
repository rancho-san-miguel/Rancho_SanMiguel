from django.urls import path
from .views import index, about, contact, blog, element, portfolio, service

urlpatterns = [
    # HOME
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('element/', element, name='element'),
    path('portfolio/', portfolio, name='portfolio'),
    path('service/', service, name='service'),

]
