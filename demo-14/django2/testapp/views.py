from urllib import response
from django.shortcuts import render
from django.views.decorators.vary import vary_on_headers
from django.utils.cache import patch_vary_headers
from django.views.decorators.cache import cache_control

# Create your views here.

@vary_on_headers('Accept-Language')
def homepage(request):
    response = render(request, "p1.html")
    patch_vary_headers(response, ['User-Agent'])
    return response

@cache_control(private=True, max_age=3600)
def about(request):
    return render(request, "p3.html")