from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1':'THIS IS SENT',
        'variable2':'THIS IS SENT',
    }
    # return HttpResponse("This Is Homepage") Now Linking With Template
    return render(request,'index.htm', context)
def about(request):
    return render(request,'about.htm')
def services(request):
    return render(request,'services.htm')

