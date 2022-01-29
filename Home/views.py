from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This Is Homepage")
def about(request):
    return HttpResponse("This Is About")