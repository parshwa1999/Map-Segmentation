from django import forms
from django.contrib.auth.models import User
from label.models import UserProfileInfo

class UserForm(forms.Modelform):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.Modelform):
    class Meta():
        model = UserProfileInfo
