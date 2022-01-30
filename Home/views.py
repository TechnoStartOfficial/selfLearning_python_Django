from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':'this is sent'
    }
    # return HttpResponse("This Is Homepage") Now Linking With Template
    return render(request,'index.htm', context)
def about(request):
    return HttpResponse("This Is About")
def services(request):
    return HttpResponse("This Is Services")
def contacts(request):
    return HttpResponse("This Is Contacts")
