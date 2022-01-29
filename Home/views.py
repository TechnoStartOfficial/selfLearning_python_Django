from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This Is Homepage")
def about(request):
    return HttpResponse("This Is About")
def services(request):
    return HttpResponse("This Is Services")
def contacts(request):
    return HttpResponse("This Is Contacts")
