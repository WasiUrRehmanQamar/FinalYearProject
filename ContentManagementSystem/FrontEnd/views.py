from django.shortcuts import render
from django.views import View
from MasterUser.models import ChildDepartment,CampusGroups,CMSUser,UserGroup,GroupMenu, Menu,Content, Group, Jobs,NewUpdates, ParentDepartment, Events, Tender, StudentNoticeBoard,FacultyProfiles,Campus
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

current_date = timezone.now()
# Create your views here
class NTUFaisalabad(View):
    
    def get(self, request):
        request.session['campus'] = 'Faisalabad'
        # print(groups)
        context = getRequiredGroups(request)
        return render(request, 'FrontEnd/templateFE/home.html', {'context':context })
        # return render(request, 'FrontEnd/home.html', {'context':context })

class NTUKarachi(View):
    
    def get(self, request):
        request.session['campus'] = 'Karachi'
        # print(groups)
        context = getRequiredGroups(request)
        return render(request, 'FrontEnd/templateFE/home.html', {'context':context })


def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    content = Content.objects.filter(menuID=menu)
    # print(content)
    context = getRequiredGroups(request)
    return render(request, 'FrontEnd/menu_detail.html', {'menu': menu, 'content': content, 'context':context })


class HomePage(View):
    
    def get(self, request):
        
        # context = getRequiredGroups(request)
        # return render(request, 'FrontEnd/home.html', {'context':context })
        return render(request, 'FrontEnd/homePage.html')
    def post(self, request):
        request.session.clear()


def jobs(request):
    jobs = Jobs.objects.filter(expiration_date__gte=current_date)
    context = getRequiredGroups(request)
    return render(request, 'FrontEnd/allJobs.html', {'jobs': jobs, 'context':context })


def job_details(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)
    # print(content)
    context = getRequiredGroups(request)
    return render(request, 'FrontEnd/job_detail.html', {'job': job, 'context':context})

def news(request):
    context = getRequiredGroups(request)
    news = NewUpdates.objects.filter(expiration_date__gte=current_date)
    return render(request, 'FrontEnd/allNews.html', {'news': news, 'context':context })


def news_details(request, news_id):
    news = get_object_or_404(NewUpdates, id=news_id)
    # print(content)
    context = getRequiredGroups(request)
    return render(request, 'FrontEnd/news_detail.html', {'news': news, 'context':context})


def events(request):
    context = getRequiredGroups(request)
    events = Events.objects.filter(expiration_date__gte=current_date)
    return render(request, 'FrontEnd/events.html', {'events': events, 'context':context })

def tender(request):
    context = getRequiredGroups(request)
    tender = Tender.objects.filter(expiration_date__gte=current_date)
    return render(request, 'FrontEnd/tender.html', {'tender': tender, 'context':context })


def NoticeBoard(request):
    context = getRequiredGroups(request)
    noticeboard = StudentNoticeBoard.objects.filter(expiration_date__gte=current_date)
    return render(request, 'FrontEnd/studentNoticeBoard.html', {'noticeboard': noticeboard, 'context':context })

def Faculty(request):
    context = getRequiredGroups(request)
    faculty = FacultyProfiles.objects.all()
    return render(request, 'FrontEnd/allFaculty.html', {'faculty': faculty, 'context':context })

def faculty_details(request, id):
    faculty = get_object_or_404(FacultyProfiles, id=id)
    # print(content)
    context = getRequiredGroups(request)
    return render(request, 'FrontEnd/faculty_details.html', {'faculty': faculty, 'context':context})

def department_details(request, id):
    department = get_object_or_404(ChildDepartment, id=id)
    # print(content)
    context = getRequiredGroups(request)
    return render(request, 'FrontEnd/department_details.html', {'department': department, 'context':context})


def getRequiredGroups(request):
    campus=request.session.get('campus')
    # print(campus)
    campus=Campus.objects.get(campusName=campus)
    campusGroups=CampusGroups.objects.filter(campus=campus)
    group_ids = campusGroups.values_list('group_id', flat=True)
    groups = Group.objects.filter(id__in=group_ids)
    departments= ParentDepartment.objects.all()
    context={'groups': groups, 'departments': departments}
    return context

