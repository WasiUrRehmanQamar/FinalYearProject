from django.contrib import admin

# Register your models here.
from .models import Campus
from .models import Content
from .models import Department
from .models import EventCategory
from .models import EventCategoryContent
from .models import EventCategoryContentWebsite
from .models import MasterUser
from .models import Menu
from .models import NewsUpdates
from .models import NewsUpdatesWebsite
from .models import RoleGroup
from .models import RoleMenu
from .models import Society
from .models import UserGroup
from .models import Website

admin.site.register(Campus)
admin.site.register(Content)
admin.site.register(Department)
admin.site.register(EventCategory)
admin.site.register(EventCategoryContent)
admin.site.register(EventCategoryContentWebsite)
admin.site.register(MasterUser)
admin.site.register(Menu)
admin.site.register(NewsUpdates)
admin.site.register(NewsUpdatesWebsite)
admin.site.register(RoleGroup)
admin.site.register(RoleMenu)
admin.site.register(Society)
admin.site.register(UserGroup)
admin.site.register(Website)

admin.site.site_header = 'Master Panel NTU CMS'