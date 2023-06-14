from django.contrib import admin

# Register your models here.
from .models import Role, CMSUser, Group, Menu, UserRole,Content,UserGroup,GroupMenu,Jobs, NewUpdates,Campus, ParentDepartment,ChildDepartment, Events, Tender, StudentNoticeBoard, CampusGroups,FacultyProfiles


class AdminRole(admin.ModelAdmin):
    list_display = ['id','roleName','active','createdBy','modifiedBy','createdat']

class AdminCMSUser(admin.ModelAdmin):
    list_display = ['id','fullName','email','password','active','createdBy','modifiedBy','createdat']

class AdminGroup(admin.ModelAdmin):
    list_display = ['id','groupName','active','createdBy','modifiedBy','createdat']

class AdminMenu(admin.ModelAdmin):
    list_display = ['id','menuName','active','createdBy','modifiedBy','createdat']


class AdminUserRole(admin.ModelAdmin):
    list_display = ['id','roleID','cmUserID','createdat','updatedat']

class AdminContent(admin.ModelAdmin):
    list_display = ['id','contentTitle','menuID','active','createdBy','modifiedBy','createdat']

class AdminUserGroup(admin.ModelAdmin):
    list_display = ['id','groupID','cmUserID','createdat']


class AdminGroupMenu(admin.ModelAdmin):
    list_display = ['id','groupID','menuID','createdat','updatedat']

class AdminJobs(admin.ModelAdmin):
    list_display = ['id','jobTitle','jobActive','createdat','updatedat','expiration_date']

class AdminNewsUpdates(admin.ModelAdmin):
    list_display = ['id','newsTitle','newsActive','createdat','updatedat','expiration_date']


class AdminCampus(admin.ModelAdmin):
    list_display = ['id','campusName','createdat','updatedat']

class AdminParentDepartment(admin.ModelAdmin):
    list_display = ['id','departmentName','departmentShortName','campusId','createdat','updatedat']

class AdminChildDepartment(admin.ModelAdmin):
    list_display = ['id','departmentName','departmentShortName','parentDepartment','createdat','updatedat']

class AdminEvents(admin.ModelAdmin):
    list_display = ['id','Image','createdat','updatedat','expiration_date']

class AdminTender(admin.ModelAdmin):
    list_display = ['id','Image','createdat','updatedat','expiration_date']

class AdminStudentNoticeBoard(admin.ModelAdmin):
    list_display = ['id','Image','createdat','updatedat','expiration_date']

class AdminCampusGroups(admin.ModelAdmin):
    list_display = ['id','campus','group','createdat','updatedat']

class AdminFacultyProfile(admin.ModelAdmin):
    list_display = ['id','name','designation','phone','email','jouralPublications','conferencePublications','address','mobile','fax','createdat']


admin.site.register(Role, AdminRole)
admin.site.register(CMSUser, AdminCMSUser)
admin.site.register(Group, AdminGroup)
admin.site.register(Menu, AdminMenu)
admin.site.register(UserRole, AdminUserRole)
admin.site.register(Content, AdminContent)
admin.site.register(UserGroup, AdminUserGroup)
admin.site.register(GroupMenu, AdminGroupMenu)
admin.site.register(Jobs, AdminJobs)
admin.site.register(NewUpdates, AdminNewsUpdates)
admin.site.register(Campus, AdminCampus)
admin.site.register(ParentDepartment, AdminParentDepartment)
admin.site.register(ChildDepartment, AdminChildDepartment)
admin.site.register(Events, AdminEvents)
admin.site.register(Tender, AdminTender)
admin.site.register(StudentNoticeBoard, AdminStudentNoticeBoard)
admin.site.register(CampusGroups, AdminCampusGroups)
admin.site.register(FacultyProfiles, AdminFacultyProfile)