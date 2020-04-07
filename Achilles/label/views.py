import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.files.storage import FileSystemStorage

import label.processing as ps

Unet_model_Road, graph_road = ps.load_Unet_road(os.path.join(settings.BASE_DIR, "static", "models", "Massachusetts_Roads_and_Building_Dataset"),
                os.path.join(settings.BASE_DIR, "static", "weights", "Massachusetts_Roads_and_Building_Dataset"))

Unet_model_Building, graph_building = ps.load_Unet_building(os.path.join(settings.BASE_DIR, "static", "models", "Massachusetts_Roads_and_Building_Dataset"),
                os.path.join(settings.BASE_DIR, "static", "weights", "Massachusetts_Roads_and_Building_Dataset"))


def index(request):
    if request.session.has_key('username'):
        return render(request, "label/homepage.html")
    else:
        return render(request, "label/index.html")

def development_tracker_response(request):
    if request.method == "POST" and len(request.FILES) != 0:
        if request.FILES['file1']:
            myfile = request.FILES['file1']
            fs = FileSystemStorage()
            if fs.exists(request.user.username + "1.png"):
                fs.delete(request.user.username + "1.png")
            filename = fs.save(request.user.username + "1.png", myfile)
            uploaded_file_url = fs.url(filename)

            if myfile.name[len(myfile.name)-3:len(myfile.name)] != "png":
                return render(request, 'label/qgis_support_app.html',{'is_not_file_valid':True})

            ps.save_image(Unet_model_Road, graph,
                os.path.join(settings.MEDIA_ROOT, request.user.username + "1.png"),
                os.path.join(settings.MEDIA_ROOT, request.user.username + "1_mask.png"))


        if request.FILES['file2']:
            myfile = request.FILES['file2']
            fs = FileSystemStorage()
            if fs.exists(request.user.username + "2.png"):
                fs.delete(request.user.username + "2.png")
            filename = fs.save(request.user.username + "2.png", myfile)
            uploaded_file_url = fs.url(filename)

            if myfile.name[len(myfile.name)-3:len(myfile.name)] != "png":
                return render(request, 'label/development_tracker_app.html',{'is_not_file_valid':True})

            ps.save_image(Unet_model_Road, graph,
                os.path.join(settings.MEDIA_ROOT, request.user.username + "2.png"),
                os.path.join(settings.MEDIA_ROOT, request.user.username + "2_mask.png"))


            return render(request, "label/development_tracker_response.html",
                {'image_url1': "/media/" + request.user.username + "1_mask.png",
                'image_url2': "/media/" + request.user.username + "2_mask.png"})
    return redirect(request.META.get('HTTP_REFERER'))


def labelme_response(request):
    print("Wrong")
    if request.method == "POST" and len(request.FILES) != 0:
        if request.FILES['file']:
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            if fs.exists(request.user.username + ".png"):
                fs.delete(request.user.username + ".png")
            filename = fs.save(request.user.username + ".png", myfile)
            uploaded_file_url = fs.url(filename)

            if myfile.name[len(myfile.name)-3:len(myfile.name)] != "png":
                return render(request, 'label/labelme_support_app.html',{'is_not_file_valid':True})

            if(request.POST.get('type') == "road"):
                ps.save_image(Unet_model_Road, graph_road,
                    os.path.join(settings.MEDIA_ROOT, request.user.username + ".png"),
                    os.path.join(settings.MEDIA_ROOT, request.user.username + "_mask.png"))
                ps.save_CSV(os.path.join(settings.MEDIA_ROOT, request.user.username + "_mask.png"),
                    os.path.join(settings.MEDIA_ROOT, request.user.username + ".csv"))

            if(request.POST.get('type') == "building"):
                ps.save_image(Unet_model_Building, graph_building,
                    os.path.join(settings.MEDIA_ROOT, request.user.username + ".png"),
                    os.path.join(settings.MEDIA_ROOT, request.user.username + "_mask.png"))
                ps.save_CSV(os.path.join(settings.MEDIA_ROOT, request.user.username + "_mask.png"),
                    os.path.join(settings.MEDIA_ROOT, request.user.username + ".csv"))

            return render(request, "label/labelme_support_response.html", {'image_url': "/media/" + request.user.username + "_mask.png"})
    return redirect(request.META.get('HTTP_REFERER'))

def qgis_response(request):
    if request.method == "POST" and len(request.FILES) != 0:
        if request.FILES['file']:
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            if fs.exists(request.user.username + ".png"):
                fs.delete(request.user.username + ".png")
            filename = fs.save(request.user.username + ".png", myfile)
            uploaded_file_url = fs.url(filename)

            if myfile.name[len(myfile.name)-3:len(myfile.name)] != "png":
                return render(request, 'label/qgis_support_app.html',{'is_not_file_valid':True})

            """
            form = ContactForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data['type'])
            print(request)
            """
            if(request.POST.get('type') == "road"):
                ps.save_image(Unet_model_Road, graph_road,
                    os.path.join(settings.MEDIA_ROOT, request.user.username + ".png"),
                    os.path.join(settings.MEDIA_ROOT, request.user.username + "_mask.png"))
                ps.save_CSV(os.path.join(settings.MEDIA_ROOT, request.user.username + "_mask.png"),
                    os.path.join(settings.MEDIA_ROOT, request.user.username + ".csv"))

            if(request.POST.get('type') == "building"):
                ps.save_image(Unet_model_Building, graph_building,
                    os.path.join(settings.MEDIA_ROOT, request.user.username + ".png"),
                    os.path.join(settings.MEDIA_ROOT, request.user.username + "_mask.png"))
                ps.save_CSV(os.path.join(settings.MEDIA_ROOT, request.user.username + "_mask.png"),
                    os.path.join(settings.MEDIA_ROOT, request.user.username + ".csv"))

            return render(request, "label/qgis_support_response.html", {'image_url': "/media/" + request.user.username + "_mask.png"})

    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def get_csv(request):
    file = open(os.path.join(settings.BASE_DIR, 'media', request.user.username + '.csv'), 'rb')
    return FileResponse(file, content_type="application/force-download")

@login_required
def get_json(request):
    file = open(os.path.join(settings.BASE_DIR, 'media', request.user.username + '.json'), 'rb')
    return FileResponse(file, content_type="application/force-download")

@login_required
def get_mask(request):
    file = open(os.path.join(settings.BASE_DIR, 'media', request.user.username + '_mask.png'), 'rb')
    return FileResponse(file, content_type="application/force-download")

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
