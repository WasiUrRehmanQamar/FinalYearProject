from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?\d{11,13}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed."
)

class Campus(models.Model):
    CampusID=models.AutoField(primary_key=True)
    CampusName=models.CharField(max_length=200)
    CampusShortName=models.CharField(max_length=200)
    CampusAddress=models.TextField()
    CampusPhone=models.CharField(max_length=200, validators=[phone_regex])
    CampusEmail=models.EmailField(max_length=200)
    CreatedBy = models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="Campus"

    def _str_(self):
        return self.name 
 
class Content(models.Model):
    ContentID=models.AutoField(primary_key=True)
    ContentTitle=models.CharField(max_length=200)
    ContentData=models.CharField(max_length=200)
    ContentImage=models.CharField(max_length=200)
    # MenuID=models.ForeignKey(Menu, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="Content"

    def _str_(self):
        return self.name 

class Department(models.Model):
    DepartmentID=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=200)
    DepartmentShortName=models.CharField(max_length=200)
    CampusID=models.ForeignKey(Campus, on_delete=models.CASCADE, db_column='CampusID')
    # ParentDepartmentID=models.ForeignKey(Department, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="Department"

    def _str_(self):
        return self.name 

class EventCategory(models.Model):
    EventCategoryID=models.AutoField(primary_key=True)
    EventCategoryName=models.CharField(max_length=200)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="EventCategory"

    def _str_(self):
        return self.name  
    
class EventCategoryContent(models.Model):
    ECContentID=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=200)
    UploadDate=models.CharField(max_length=200)
    DueDate=models.CharField(max_length=200)
    Category=models.CharField(max_length=200)
    EventContent=models.CharField(max_length=200)
    EventCategoryID=models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="EventCategoryContent"

    def _str_(self):
        return self.name

class EventCategoryContentWebsite(models.Model):
    ECContentWebsiteID=models.AutoField(primary_key=True)
    ECContentID=models.ForeignKey(EventCategoryContent, on_delete=models.CASCADE)
    # WebsiteID=models.ForeignKey(Website, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="EventCategoryContentWebsite"

    def _str_(self):
        return self.name    

class MasterUser(models.Model):
    MasterUserID=models.AutoField(primary_key=True)
    FullName=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="MasterUser"

    def _str_(self):
        return self.name      

class Menu(models.Model):
    MenuID=models.AutoField(primary_key=True)
    MenuName=models.CharField(max_length=200)
    MenuLink=models.CharField(max_length=200)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="Menu"
        
    def _str_(self):
        return self.name      
    
class NewsUpdates(models.Model):
    NewsUpdatesID=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=200)
    NewsContent=models.CharField(max_length=200)
    UploadDate=models.CharField(max_length=200)
    DueDate=models.CharField(max_length=200)
    TitleImage=models.CharField(max_length=200)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="NewsUpdates"

    def _str_(self):
        return self.name      
    
class NewsUpdatesWebsite(models.Model):
    NewsUpdatesWebsiteID=models.AutoField(primary_key=True)
    NewsUpdatesID=models.ForeignKey(NewsUpdates, on_delete=models.CASCADE)
    # WebsiteID=models.ForeignKey(Website, on_delete=models.CASCADE)
    DepartmentID=models.ForeignKey(Department, on_delete=models.CASCADE)
    # SocietyID=models.ForeignKey(Society, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="NewsUpdatesWebsite"

    def _str_(self):
        return self.name      
    
class RoleGroup(models.Model):
    UserRoleGroupID=models.AutoField(primary_key=True)
    # UserRoleID=models.ForeignKey(UserRole, on_delete=models.CASCADE)
    # UserGroupID=models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="RoleGroup"

    def _str_(self):
        return self.name      
    
class RoleMenu(models.Model):
    UserRoleID=models.AutoField(primary_key=True)
    MenuID=models.ForeignKey(Menu, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="RoleMenu"

    def _str_(self):
        return self.name      

class Society(models.Model):
    SocietyID=models.AutoField(primary_key=True)
    SocietyName=models.CharField(max_length=200)
    SocietyShortName=models.CharField(max_length=200)
    CampusID=models.ForeignKey(Campus, on_delete=models.CASCADE)
    DepartmentID=models.ForeignKey(Department, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="Society"

    def _str_(self):
        return self.name   

class UserGroup(models.Model):
    UserGroupID=models.AutoField(primary_key=True)
    UserGroupName=models.CharField(max_length=200)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="UserGroup"

    def _str_(self):
        return self.name
    
class UserRole(models.Model):
    UserRoleID=models.AutoField(primary_key=True)
    UserRoleName=models.CharField(max_length=200)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="UserRole"

    def _str_(self):
        return self.name
    
class Website(models.Model):
    WebsiteID=models.AutoField(primary_key=True)
    WebsiteName=models.CharField(max_length=200)
    WebsiteShortName=models.CharField(max_length=200)
    CampusID=models.ForeignKey(Campus, on_delete=models.CASCADE)
    DepartmentID=models.ForeignKey(Department, on_delete=models.CASCADE)
    SocietyID=models.ForeignKey(Society, on_delete=models.CASCADE)
    # ResearchGroupID=models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    # ConferenceID=models.ForeignKey(Conference, on_delete=models.CASCADE)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="Website"
        
    def _str_(self):
        return self.name

class ResearchGroup(models.Model):
    ResearchGroupID=models.AutoField(primary_key=True)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="ResearchGroup"
        
    def _str_(self):
        return self.name

class Conference(models.Model):
    ConferenceID=models.AutoField(primary_key=True)
    CreatedBy=models.CharField(max_length=200)
    CreatedDate=models.DateTimeField(auto_now_add=True)
    ModifiedBy=models.CharField(max_length=200)
    ModifiedDate=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=1)

    class Meta:
        verbose_name_plural="Conference"
        
    def _str_(self):
        return self.name        