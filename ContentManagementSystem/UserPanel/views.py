from django.shortcuts import render,redirect
from urllib.parse import urlencode
from django.urls import reverse
from geopy.geocoders import Nominatim
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import json
from MasterUser.models import CMSUser,UserGroup,GroupMenu, Menu,Content, Group
# Create your views here.
from django.shortcuts import redirect
from django.views import View


class MasterLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if "email" not in request.session:
            return render(request, 'UserPanel/login.html')
        return super().dispatch(request, *args, **kwargs)


class UserLogin(View):
    
    def get(self, request):
        if "email" in request.session:
            email=request.session.get('email')
            password=request.session.get('password')
            try:
                # Retrieve CMSUser based on email and password
                cms_user = CMSUser.objects.get(email=email, password=password)
                request.session['fullName'] = cms_user.fullName
                request.session['email'] = cms_user.email
                request.session['password'] = cms_user.password
                # Get all UserGroup objects associated with the CMSUser
                user_groups = UserGroup.objects.filter(cmUserID=cms_user)

                # Create a list to store the group and menu data
                group_data = []

                # Iterate over UserGroup objects
                for user_group in user_groups:
                    group = user_group.groupID

                    # Fetch GroupMenu objects for the current group
                    group_menus = GroupMenu.objects.filter(groupID=group)

                    # Create a list to store the menus for the current group
                    menu_data = []

                    # Iterate over GroupMenu objects
                    for group_menu in group_menus:
                        menu = group_menu.menuID
                        menu_data.append(menu)

                    # Append group and menu data to the main list
                    group_data.append((group, menu_data))

                # Pass the data to the template for rendering
                context = {
                    'group_data': group_data,
                    'cms_user':cms_user
                        }
                return render(request, 'UserPanel/home.html', context)

            except CMSUser.DoesNotExist:
                # Handle the case where email and password do not match
                error_message = "Invalid email or password."
                return render(request, 'UserPanel/login.html', {'error_message': error_message})
            
        else:
            return render(request, 'UserPanel/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Retrieve CMSUser based on email and password
            cms_user = CMSUser.objects.get(email=email, password=password)
            request.session['fullName'] = cms_user.fullName
            request.session['email'] = cms_user.email
            request.session['password'] = cms_user.password
            # Get all UserGroup objects associated with the CMSUser
            user_groups = UserGroup.objects.filter(cmUserID=cms_user)

            # Create a list to store the group and menu data
            group_data = []

            # Iterate over UserGroup objects
            for user_group in user_groups:
                group = user_group.groupID

                # Fetch GroupMenu objects for the current group
                group_menus = GroupMenu.objects.filter(groupID=group)

                # Create a list to store the menus for the current group
                menu_data = []

                # Iterate over GroupMenu objects
                for group_menu in group_menus:
                    menu = group_menu.menuID
                    menu_data.append(menu)

                # Append group and menu data to the main list
                group_data.append((group, menu_data))

            # Pass the data to the template for rendering
            context = {
                'group_data': group_data,
                'cms_user':cms_user
                       }
            return render(request, 'UserPanel/home.html', context)

        except CMSUser.DoesNotExist:
            # Handle the case where email and password do not match
            error_message = "Invalid email or password."
            return render(request, 'UserPanel/login.html', {'error_message': error_message})
        
class UserLogut(View):
    
    def get(self, request):
        request.session.clear()
        response = HttpResponse(render(request, 'UserPanel/login.html'))
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'  # Set cache control headers
        return response
    
        # return render(request, 'UserPanel/login.html')

    def post(self, request):
        request.session.clear()
        response = HttpResponse(render(request, 'UserPanel/login.html'))
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'  # Set cache control headers
        return response
    
class ManageContent(MasterLoginRequiredMixin,View):
    
    def get(self, request,groupName, menuName):
        menuObject= Menu.objects.filter(id=menuName).first()
        content= Content.objects.filter(menuID=menuObject).first()
        context = {
                'content': content,
                'menuObject':menuObject
                       }
        return render(request, 'UserPanel/createContent.html',context)

    def post(self, request):
        return redirect('user-panel')
    

class CreateContent(MasterLoginRequiredMixin,View):
    
    def get(self, request):
        
        # context = {
        #         'content': content,
        #                }
        # return render(request, 'UserPanel/createContent.html',context)
        pass
    def post(self, request):
        id = request.POST.get('id')
        menuObjectId = request.POST.get('menuObject')
        title = request.POST.get('title')
        description = request.POST.get('description')
        images=request.FILES.getlist('images')
        # print('images',images)
        if len(images) != 0:
            image = images[0]
        else:
            image='None'
        userName=request.session.get('fullName')
        menuObject=Menu.objects.filter(id=menuObjectId).first()
        if id!='':
            content= Content.objects.filter(id=id).first()
            content.contentTitle=title
            content.contentData=description
            content.contentImage = image
            content.modifiedBy=userName
            content.save()
        else:
            content = Content.objects.create(
            contentTitle=title,
            contentData=description,
            contentImage = image,
            createdBy=userName,
            modifiedBy=userName,
            menuID=menuObject
            )
            content.save()
        return redirect('user-panel')