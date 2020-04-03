import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.session.has_key('username'):
        return render(request, "label/homepage.html")
    else:
        return render(request, "label/index.html")

def qgis_response(request):
    if request.method == "POST" and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        if fs.exists(request.user.username + ".png"):
            fs.delete(request.user.username + ".png")
        filename = fs.save(request.user.username + ".png", myfile)
        uploaded_file_url = fs.url(filename)

        if myfile.name[len(myfile.name)-3:len(myfile.name)] != "png":
            return render(request, "label/qgis_support_app.html",{'is_not_file_valid':True})

        return render(request, "label/qgis_support_response.html", {'image_url': uploaded_file_url })

    return render(request, "label/qgis_support_app.html")


def development_tracker(request):
    if request.session.has_key('username'):
        return render(request, "label/development_tracker_app.html")
    else:
        return render(request, "label/development_tracker_about.html")

def qgis_support(request):
    if request.session.has_key('username'):
        return render(request, "label/qgis_support_app.html")
    else:
        return render(request, "label/qgis_support_about.html")

def labelme_support(request):
    if request.session.has_key('username'):
        return render(request, "label/labelme_support_app.html")
    else:
        return render(request, "label/labelme_support_about.html")

@login_required
def homepage_welcome(request, username):
    return render(request, "label/homepage.html", {'user' : username})

@login_required
def homepage(request):
    return render(request, "label/homepage.html", {'user' : "$"})

@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['username']
    except:
       pass
    return render(request, "label/logout.html")

def user_login(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return homepage(request)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                request.session['username'] = username
                return homepage_welcome(request, user)

        else:
            return render(request, 'label/login.html', {'incorrect' : 'Incorrect Username or Password'})

    else:
        return render(request, 'label/login.html')
