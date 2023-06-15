from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from MasterUser.models import CMSUser,UserGroup,GroupMenu, Menu,Content, Group, Campus, CampusGroups,FacultyProfiles
from django.contrib.auth.hashers import make_password
import random
from django.shortcuts import redirect
from django.views import View


class MasterLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if "Masteremail" not in request.session:
            return redirect('master-login')  # Replace 'master_login' with your actual login URL
        return super().dispatch(request, *args, **kwargs)


class AdminLogin(View):
    
    def get(self, request):
        if "Masteremail" in request.session:
            return render(request, 'MasterPanel/home.html')
        # request.session.clear()
        return render(request, 'MasterPanel/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # print(email,password)
        try:
            if email=='admin@gmail.com' and password=='12345':
                request.session['Masteremail'] = email
                request.session['Adminname'] = 'Mr. Admin'
            # user = User.objects.get(email=email, password=password)
            # print(user)
            # if user is not None:
                # error_message = "Good"
                return render(request, 'MasterPanel/home.html')
                # except CMSUser.DoesNotExist:
            else:
                error_message = "Invalid Email Password"
                return render(request, 'MasterPanel/login.html', {'error_message': error_message})
        except Exception as e:
            print(e)
            return render(request, 'MasterPanel/login.html')
            


class MasterUsers(MasterLoginRequiredMixin,View):

    def get(self, request):
        allUsers = CMSUser.objects.all().order_by('-id')
        for user in allUsers:
            encrypted_password = make_password(user.password)
            random_start_index = random.randint(0, len(encrypted_password) - 10)
            user.password = encrypted_password[random_start_index:random_start_index + 10]
        context = {
                'allUsers': allUsers,
                # 'cms_user':cms_user
                       }
        return render(request, 'MasterPanel/allUsers.html', context)
    

class MasterGroups(MasterLoginRequiredMixin,View):

    def get(self, request):
        allGroups = Group.objects.all().order_by('-id')
        context = {
                'allGroups': allGroups,
                # 'cms_user':cms_user
                       }
        return render(request, 'MasterPanel/allGroups.html', context)
        

    
class MasterMenus(MasterLoginRequiredMixin,View):

    def get(self, request):
        allMenus = Menu.objects.all().order_by('-id')
        # print(allMenus)
        context = {
                'allMenus': allMenus,
                # 'cms_user':cms_user
                       }
        return render(request, 'MasterPanel/allMenus.html', context)
        

    
class AddNewUser(MasterLoginRequiredMixin,View):

    def get(self, request):
        return render(request, 'MasterPanel/addNewUser.html')
        
    def post(self, request):
        fullName = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        adminUser=request.session.get('Adminname')
        try:
            userObject = CMSUser.objects.get(email=email)
            # if userObject is not None:
            error_message = "User with "+email+ " already Exists"
            return render(request, 'MasterPanel/addNewUser.html', {'error_message': error_message})
            # else:
            #     print("Not exist")
            #     return render(request, 'MasterPanel/addNewUser.html')
        except:
            newUserObject = CMSUser.objects.create(
            fullName=fullName,
            email=email,
            password=password,
            createdBy=adminUser,
            modifiedBy=adminUser,
            )
            newUserObject.save()
            return redirect('/master-users')
            # return render(request, 'MasterPanel/addNewUser.html')
        

class AddNewGroup(MasterLoginRequiredMixin,View):

    def get(self, request):
        return render(request, 'MasterPanel/addNewGroup.html')
        
    def post(self, request):
        groupName = request.POST.get('name')
        is_faisalabad_checked = 'Faisalabad' in request.POST
        is_karachi_checked = 'Karachi' in request.POST
        adminUser=request.session.get('Adminname')
        try:
            groupObject = Group.objects.get(groupName=groupName)
            # if userObject is not None:
            error_message = "Group with "+groupName+ " name already exists."
            return render(request, 'MasterPanel/addNewGroup.html', {'error_message': error_message})
            # else:
            #     print("Not exist")
            #     return render(request, 'MasterPanel/addNewUser.html')
        except:
            newGroupObject = Group.objects.create(
            groupName=groupName,
            createdBy='Mr. Admin',
            modifiedBy='Mr. Admin',
            )
            newGroupObject.save()
            if is_faisalabad_checked:
                faisalabad= Campus.objects.get(campusName='Faisalabad')
                faisalabadGroupObject = CampusGroups.objects.create(
                campus=faisalabad,
                group=newGroupObject,
                )
                faisalabadGroupObject.save()

            if is_karachi_checked:
                karachi= Campus.objects.get(campusName='Karachi')
                karachiGroupObject = CampusGroups.objects.create(
                campus=karachi,
                group=newGroupObject
                )
                karachiGroupObject.save()
 
            return redirect('/master-groups')
            # return render(request, 'MasterPanel/addNewUser.html')


class AddNewMenu(MasterLoginRequiredMixin,View):

    def get(self, request):
        allGroups= Group.objects.all().order_by('-id')
        return render(request, 'MasterPanel/addNewMenu.html',{'allGroups':allGroups})
        
    def post(self, request):
        menuName = request.POST.get('name')
        group=request.POST.get('group')
        adminUser=request.session.get('Adminname')
        try:
            menuObject = Menu.objects.get(menuName=menuName)
            # if userObject is not None:
            error_message = "Menu with "+menuName+ " name already exists."
            allGroups= Group.objects.all().order_by('-id')
            return render(request, 'MasterPanel/addNewMenu.html', {'error_message': error_message,'allGroups':allGroups})
            # else:
            #     print("Not exist")
            #     return render(request, 'MasterPanel/addNewUser.html')
        except:
            newMenuObject = Menu.objects.create(
            menuName=menuName,
            createdBy='Mr. Admin',
            modifiedBy='Mr. Admin',
            )
            groupObject=Group.objects.get(id=group)
            newMenuObject.save()
            newMenuGroupObject = GroupMenu.objects.create(
            groupID=groupObject,
            menuID=newMenuObject,
            )
            newMenuGroupObject.save()
            return redirect('/master-menus')
            # return render(request, 'MasterPanel/addNewUser.html')


class MasterMenuGroup(MasterLoginRequiredMixin,View):

    def get(self, request):
        groups = Group.objects.all()
        group_data = []
        
        for group in groups:
            menus = group.groupmenu_set.all().values('menuID__menuName')
            group_data.append({'group': group, 'menus': menus})
        return render(request, 'MasterPanel/allMenuGroup.html', {'group_data': group_data})
        

class AddNewMenuGroup(MasterLoginRequiredMixin,View):

    def get(self, request):
        allGroups= Group.objects.all().order_by('-id')
        allMenus = Menu.objects.all().order_by('-id')

        context = {
                'allGroups': allGroups,
                'allMenus':allMenus
                       }
        return render(request, 'MasterPanel/addNewMenuGroup.html', context)
        # return render(request, 'MasterPanel/addNewMenuGroup.html')
        
    def post(self, request):
        menu = request.POST.get('menu')
        group = request.POST.get('group')
        print(menu,group)
        # return redirect('/add-new-menu-group')
        adminUser=request.session.get('Adminname')
        try:
            menugroupObject = GroupMenu.objects.get(groupID=group,menuID=menu)
            # if userObject is not None:
            error_message = "Menu already exists in this Group"
            allGroups= Group.objects.all().order_by('-id')
            allMenus = Menu.objects.all().order_by('-id')

            context = {
                    'allGroups': allGroups,
                    'allMenus':allMenus,
                    'error_message':error_message
                        }
            return render(request, 'MasterPanel/addNewMenuGroup.html', context)
            # return render(request, 'MasterPanel/addNewMenuGroup.html', {'error_message': error_message})
            # else:
            #     print("Not exist")
            #     return render(request, 'MasterPanel/addNewUser.html')
        except:
            menuObject=Menu.objects.get(id=menu)
            groupObject=Group.objects.get(id=group)
            newMenuGroupObject = GroupMenu.objects.create(
            groupID=groupObject,
            menuID=menuObject,
            )
            newMenuGroupObject.save()
            
            return redirect('/master-menu-group')
            # return render(request, 'MasterPanel/addNewUser.html')
            

class MasterUserGroup(MasterLoginRequiredMixin,View):

    def get(self, request):
        users = CMSUser.objects.all()
        return render(request, 'MasterPanel/allUserGroup.html', {'users': users})
        


class AddNewUserGroup(MasterLoginRequiredMixin,View):

    def get(self, request):
        allGroups= Group.objects.all().order_by('-id')
        allUsers = CMSUser.objects.all().order_by('-id')

        context = {
                'allGroups': allGroups,
                'allUsers':allUsers
                       }
        return render(request, 'MasterPanel/addNewUserGroup.html', context)
        # return render(request, 'MasterPanel/addNewMenuGroup.html')
        
    def post(self, request):
        user = request.POST.get('user')
        group = request.POST.get('group')
        print(user,group)
        # return redirect('/add-new-user-group')
        # adminUser=request.session.get('Adminname')
        try:
            userGroupObject = UserGroup.objects.get(groupID=group,cmUserID=user)
            # if userObject is not None:
            error_message = "Group already assigned to this User."
            allGroups= Group.objects.all().order_by('-id')
            allUsers = CMSUser.objects.all().order_by('-id')

            context = {
                    'allGroups': allGroups,
                    'allUsers':allUsers,
                    'error_message':error_message
                        }
            return render(request, 'MasterPanel/addNewUserGroup.html', context)
            # return render(request, 'MasterPanel/addNewMenuGroup.html', {'error_message': error_message})
            # else:
            #     print("Not exist")
            #     return render(request, 'MasterPanel/addNewUser.html')
        except:
            userObject=CMSUser.objects.get(id=user)
            groupObject=Group.objects.get(id=group)
            newUserGroupObject = UserGroup.objects.create(
            groupID=groupObject,
            cmUserID=userObject,
            )
            # groupID=group,cmUserID=user
            newUserGroupObject.save()
            
            return redirect('/master-user-group')
            # return render(request, 'MasterPanel/addNewUser.html')
            

class MasterLogout(View):
    def get(self, request):
        request.session.clear()
        return render(request, 'MasterPanel/login.html')
