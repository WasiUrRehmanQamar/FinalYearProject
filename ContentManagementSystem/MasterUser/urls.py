from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('master-login', AdminLogin.as_view(), name='master-login'),
    path('master-home', AdminLogin.as_view(), name='master-home'),

    path('master-users', MasterUsers.as_view(), name='master-users'),
    path('master-groups', MasterGroups.as_view(), name='master-groups'),
    path('master-menus', MasterMenus.as_view(), name='master-menus'),
    
    
    path('add-new-user', AddNewUser.as_view(), name='add-new-user'),
    path('add-new-group', AddNewGroup.as_view(), name='add-new-group'),
    path('add-new-menu', AddNewMenu.as_view(), name='add-new-menu'),
    path('add-new-menu-group', AddNewMenuGroup.as_view(), name='add-new-menu-group'),
    path('add-new-user-group', AddNewUserGroup.as_view(), name='add-new-user-group'),

    path('master-menu-group', MasterMenuGroup.as_view(), name='master-menu-group'),
    path('master-user-group', MasterUserGroup.as_view(), name='master-user-group'),

    path('master-logout', MasterLogout.as_view(), name='master-logout'),
    
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)