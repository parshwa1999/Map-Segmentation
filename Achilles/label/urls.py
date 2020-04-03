from django.urls import path
from label import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.homepage, name='homepage'),
    path('user_login/',  views.user_login, name='user_login'),
    path('development_tracker/',  views.development_tracker, name='developmentTracker'),
    path('qgis_support/',  views.qgis_support, name='qgisSupport'),
    path('labelme_support/',  views.labelme_support, name='labelmeSupport'),
    path('qgis_support_response/',  views.qgis_response, name='qgisResponse'),
]
