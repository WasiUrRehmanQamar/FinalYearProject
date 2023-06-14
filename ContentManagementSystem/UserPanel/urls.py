from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from . import views
urlpatterns = [

    path('user-panel', UserLogin.as_view(), name='user-panel'),
    path('user-logout', UserLogut.as_view(), name='user-logout'),
    path('menu/category/<slug:groupName>/<slug:menuName>', ManageContent.as_view(), name='menu/category'),
    path('create-content', CreateContent.as_view(), name='create-content'),
    
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)