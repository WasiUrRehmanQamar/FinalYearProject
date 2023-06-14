from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from . import views
urlpatterns = [

    path('ntu-faisalabad', NTUFaisalabad.as_view(), name='ntu-faisalabad'),
    path('', NTUFaisalabad.as_view(), name=''),
    path('karachi', NTUKarachi.as_view(), name='karachi'),
    # path('', HomePage.as_view(), name=''),
    path('menu/<int:menu_id>', menu_detail, name='menu_detail'),
    path('jobs', jobs, name='jobs'),
    path('job_details/<int:job_id>', job_details, name='job_details'),
    path('news', news, name='news'),
    path('news_details/<int:news_id>', news_details, name='news_details'),
    path('events', events, name='events'),
    path('tender', tender, name='tender'),
    path('student-notice-board', NoticeBoard, name='student-notice-board'),
    path('faculty', Faculty, name='faculty'),
    path('faculty_details/<int:id>', faculty_details, name='faculty_details'),
    path('department_details/<int:id>', department_details, name='department_details'),
    
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)