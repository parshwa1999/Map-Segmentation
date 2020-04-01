from django.urls import path
from label import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.homepage, name='homepage'),
    path('user_login/',  views.user_login, name='user_login'),
]
