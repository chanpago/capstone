from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'capstones\\index.html')

def fileUpload(request):
    return render(request, 'capstones\\fileUpload.html')

def progress(request):
    return render(request, 'capstones\\progress.html')

def detectResult(request):
    return render(request, 'capstones\\detectResult.html')
    
def pipeInfo(request):
    return render(request, 'capstones\\pipeInfo.html')

def pipeCost(request):
    return render(request, 'capstones\\pipeCost.html')