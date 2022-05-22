"""capstone01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from capstones import views
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('fileUpload/',views.fileUpload, name='fileUpload'),
    path('progress/',views.progress, name='progress'),
    path('detectResult/',views.detectResult, name='detectResult'),
    path('pipeInfo/',views.pipeInfo, name='pipeInfo'),
    path('pipeCost/',views.pipeCost, name='pipeCost'),
    path('generate/',views.generate, name='generate'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



