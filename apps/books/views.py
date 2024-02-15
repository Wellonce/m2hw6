from django.shortcuts import render, HttpResponse

def home_view(request):
    return HttpResponse (request, "Home Page is here")