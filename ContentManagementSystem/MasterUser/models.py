from django.db import models
from tinymce import models as tinymce_models
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

class Role(models.Model):
    roleName    = models.CharField(max_length=200)
    active      =models.BooleanField(default=True)
    createdBy   =models.CharField(max_length=200)
    modifiedBy  =models.CharField(max_length=200)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    
    class Meta:
        verbose_name_plural="Role"
    def __str__(self):
        return self.roleName
    
class CMSUser(models.Model):
    fullName    =models.CharField(max_length=200)
    email       =models.CharField(max_length=200)
    password    =models.CharField(max_length=200)
    active      =models.BooleanField(default=True)
    createdBy   =models.CharField(max_length=200)
    modifiedBy  =models.CharField(max_length=200)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    
    class Meta:
        verbose_name_plural="User"

    def _str_(self):
        return self.fullName  

class Campus(models.Model):
    
    campusName = models.CharField(max_length=200,unique=True)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    class Meta:
         verbose_name_plural="Campus"
    def __str__(self):
        return self.campusName 

class Group(models.Model):
    groupName   =models.CharField(max_length=200)
    active      =models.BooleanField(default=True)
    createdBy   =models.CharField(max_length=200)
    modifiedBy  =models.CharField(max_length=200)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    
    class Meta:
        verbose_name_plural="Group"

    def __str__(self):
        return self.groupName
    

class Menu(models.Model):
    menuName    =models.CharField(max_length=200)
    active      =models.BooleanField(default=True)
    createdBy   =models.CharField(max_length=200)
    modifiedBy  =models.CharField(max_length=200)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name_plural="Menu"
        
    def _str_(self):
        return self.menuName

class Content(models.Model):
    contentTitle    =models.CharField(max_length=200)
    contentImage    =models.ImageField(upload_to='upload/content/')
    contentData     =tinymce_models.HTMLField()
    menuID          =models.ForeignKey(Menu, on_delete=models.CASCADE)
    active          =models.BooleanField(default=True)
    createdBy       =models.CharField(max_length=200)
    modifiedBy      =models.CharField(max_length=200)
    createdat       =models.DateTimeField(db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat       =models.DateTimeField(db_column='updatedAt', blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name_plural="Content"

    def _str_(self):
        return self.contentTitle 


class UserRole(models.Model):
    
    roleID = models.ForeignKey(Role, on_delete=models.CASCADE)
    cmUserID = models.ForeignKey(CMSUser, on_delete=models.CASCADE)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    
    class Meta:
         verbose_name_plural="UserRole"


class UserGroup(models.Model):
    
    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)
    cmUserID = models.ForeignKey(CMSUser, on_delete=models.CASCADE)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    
    class Meta:
         verbose_name_plural="UserGroup"


class GroupMenu(models.Model):
    
    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)
    menuID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    
    class Meta:
         verbose_name_plural="GroupMenu"



    




class ParentDepartment(models.Model):
    
    departmentName = models.CharField(max_length=200,unique=True)
    departmentShortName = models.CharField(max_length=200,unique=True)
    campusId = models.ForeignKey(Campus, on_delete=models.CASCADE)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    
    class Meta:
         verbose_name_plural="ParentDepartment"
    def __str__(self):
        return self.departmentName
    

class ChildDepartment(models.Model):
    
    departmentName = models.CharField(max_length=200,unique=True)
    departmentShortName = models.CharField(max_length=200,unique=True)
    parentDepartment = models.ForeignKey(ParentDepartment, on_delete=models.CASCADE)
    deptDescription =tinymce_models.HTMLField(null=False, blank=False,default='N/A')
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    
    class Meta:
         verbose_name_plural="ChildDepartment"
    def __str__(self):
        return self.departmentName 

class Jobs(models.Model):
    
    jobTitle       =models.CharField(max_length=200)
    # jobImage    =models.ImageField(upload_to='upload/jobs/',blank=False, null=False, default='')
    jobDescription =tinymce_models.HTMLField()
    jobActive      =models.BooleanField(default=True)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    expiration_date = models.DateTimeField(max_length=100, blank=False, null=False, default='')

    
    class Meta:
         verbose_name_plural="Jobs"
    def _str_(self):
        return self.jobTitle 
    def clean(self):
        if self.expiration_date <= timezone.now():
            raise ValidationError("Expiration date must be greater than the current date.")
    def save(self, *args, **kwargs):
        self.clean()  # Run the clean method before saving
        super().save(*args, **kwargs)




class NewUpdates(models.Model):
    
    newsTitle       =models.CharField(max_length=200)
    newsContent =tinymce_models.HTMLField()
    newsActive      =models.BooleanField(default=True)
    titleImage = models.ImageField(upload_to='upload/newupdates/')
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    expiration_date = models.DateTimeField(max_length=100, blank=False, null=False, default='')

    
    class Meta:
         verbose_name_plural="NewsUpdates"
    def _str_(self):
        return self.newsTitle 
    def clean(self):
        if self.expiration_date <= timezone.now():
            raise ValidationError("Expiration date must be greater than the current date.")
    def save(self, *args, **kwargs):
        self.clean()  # Run the clean method before saving
        super().save(*args, **kwargs)




class StudentNoticeBoard(models.Model):
    
    # contents =tinymce_models.HTMLField()
    Image    =models.ImageField(upload_to='upload/noticeboard/',blank=False, null=False, default='')
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    expiration_date = models.DateTimeField(max_length=100, blank=False, null=False, default='')

    class Meta:
         verbose_name_plural="StudentNoticeBoard"
 
    def clean(self):
        if self.expiration_date <= timezone.now():
            raise ValidationError("Expiration date must be greater than the current date.")
    def save(self, *args, **kwargs):
        self.clean()  # Run the clean method before saving
        super().save(*args, **kwargs)




    
class Events(models.Model):
    
    # contents =tinymce_models.HTMLField()
    Image    =models.ImageField(upload_to='upload/events/',blank=False, null=False, default='')
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    expiration_date = models.DateTimeField(max_length=100, blank=False, null=False, default='')

    class Meta:
         verbose_name_plural="Events"
   
    
    def clean(self):
        if self.expiration_date <= timezone.now():
            raise ValidationError("Expiration date must be greater than the current date.")
    def save(self, *args, **kwargs):
        self.clean()  # Run the clean method before saving
        super().save(*args, **kwargs)

    
class Tender(models.Model):
    
    # contents =tinymce_models.HTMLField()
    Image    =models.ImageField(upload_to='upload/tender/',blank=False, null=False, default='')
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    expiration_date = models.DateTimeField(max_length=100, blank=False, null=False, default='')

    class Meta:
         verbose_name_plural="Tender"
    
    def clean(self):
        if self.expiration_date <= timezone.now():
            raise ValidationError("Expiration date must be greater than the current date.")
    def save(self, *args, **kwargs):
        self.clean()  # Run the clean method before saving
        super().save(*args, **kwargs)
    

class CampusGroups(models.Model):
    
    campus =models.ForeignKey(Campus, on_delete=models.CASCADE)
    group =models.ForeignKey(Group, on_delete=models.CASCADE)
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)
    

class FacultyProfiles(models.Model):
    
    name       =models.CharField(max_length=200)
    Image    =models.ImageField(upload_to='upload/faculty/')
    designation= models.CharField(max_length=200)
    jouralPublications= models.IntegerField()
    conferencePublications= models.IntegerField()
    address       =models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    description =tinymce_models.HTMLField()
    
    createdat = models.DateTimeField(
        db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat = models.DateTimeField(
        db_column='updatedAt', blank=True, null=True, auto_now=True)

    class Meta:
         verbose_name_plural="Faculty"
    def _str_(self):
        return self.name 