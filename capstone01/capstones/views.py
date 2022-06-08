from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from . import models
from codes import system
import os
# Create your views here.


def index(request):
    DeleteAllFiles('media\\pipeimages')
    DeleteAllFiles('capstones\\static\\result')
    return render(request, 'capstones\\index.html')

def fileUpload(request):
    print("?")
    if request.method =='POST':
        
        
        uploadedFile = request.FILES.getlist('uploadedFile')

        #saving the information in the database
        for img in uploadedFile:
            document = models.Document(
                uploadedFile = img
            )
            document.save()
            documents = models.Document.objects.all()
            
        system.detect_process_run()

    return render(request, 'capstones\\fileUpload.html') 

def progress(request):
    fileUpload(request)
    return render(request, 'capstones\\progress.html')

def detectResult(request):
    return render(request, 'capstones\\detectResult.html')
    
def pipeInfo(request):
    return render(request, 'capstones\\pipeInfo.html')

def pipeCost(request):
    return render(request, 'capstones\\pipeCost.html')

def generate(request):
    return render(request, 'capstones\\generate.html')

def DeleteAllFiles(filepath):
    if os.path.exists(filepath):
        for file in os.scandir(filepath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'