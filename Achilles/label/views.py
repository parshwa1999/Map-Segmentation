from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    if request.session.has_key('username'):
        return render(request, "label/homepage.html")        
    else:
        return render(request, "label/index.html")

@login_required
def homepage_welcome(request, username):
    print(username)
    return render(request, "label/homepage.html", {'user' : username})

@login_required
def homepage(request):
    return render(request, "label/homepage.html")

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
