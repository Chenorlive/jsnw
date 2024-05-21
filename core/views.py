from typing import Any
from django.http import FileResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from core.models import ( 
    Member, Blog, Report, Question, BlogCategory, Media,
    MediaCategory, DistrictE, Town, DistrictA
)
from django.views import generic
from datetime import datetime, timedelta
from .forms import (
    QuestionForm, BlogForm, ReportForm, MediaForm,
)


# Create your views here.


def index(request):

    blog = Blog.objects.all().order_by('created_at')[:4]
    district_E = DistrictE.objects.all()
    district_A = DistrictA.objects.all()
    town = Town.objects.all()

    context = {'blog': blog, 'district': district_E, 'town': town}
    return render(request=request, template_name="pages/index.html", context=context)


def about(request):
    return render(request=request, template_name="pages/about1.html")

def donate(request):

    return render(request=request, template_name="pages/about1.html")


def aboutDistrict(request):
    return render(request=request, template_name="pages/about.html")

def contact(request):
    return render(request=request, template_name="pages/contact.html")


def initiative(request, pk):
    context = {'obb' : pk}
    return render(request=request, template_name="pages/initiative.html",
                  context=context)



class GalleryListView(generic.ListView):
    model = Media
    paginate_by = 30
    context_object_name = 'objects'
    extra_context = {'year': datetime.now().year, 'title': 'Gallery', 'list': [1,2,3,4,5]}
    template_name = 'pages/gallery.html'

    def get_queryset(self):
        category = self.kwargs['category']
        obj = Media.objects.filter(category__pk=category).order_by('created_at')
       
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obb'] = self.kwargs['category']
        return context


class BlogListView(generic.ListView):
    queryset = Blog.objects.all()
    model = Blog
    paginate_by = 30
    context_object_name = 'object'
    extra_context = {'year': datetime.now().year, 'title': 'News', 'list': [1,2,3,4,5]}
    template_name = 'pages/blogs.html'


class QuestionListView(generic.ListView):
    queryset = Question.objects.filter(is_fqa=False)
    model = Question
    paginate_by = 30
    context_object_name = 'object'
    extra_context = {'year': datetime.now().year, 'title': 'Question', 'list': [1,2,3,4,5]}
    template_name = 'pages/questions.html'

    


class FAQListView(generic.ListView):
    queryset = Question.objects.filter(is_fqa=True)
    model = Question
    paginate_by = 30
    context_object_name = 'object'
    extra_context = {'year': datetime.now().year, 'title': 'FAQ', 'list': [1,2,3,4,5]}
    template_name = 'pages/faq.html'



#ReportListView
class ReportListView(generic.ListView):
    model = Report
    paginate_by = 30
    context_object_name = 'objects'
    extra_context = {'year': datetime.now().year, 'title': 'Report', 'list': [1,2,3,4,5]}
    template_name = 'pages/reports.html'

    def get_queryset(self):
        category = self.kwargs['category']
        obj = Report.objects.filter(category__pk=category).order_by('created_at')
       
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obb'] = self.kwargs['category']
        return context
    
  

def createMember(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        address = request.POST['address']
        comment = request.POST['comment']
        
        member = Member(
            name = name, number = number, address = address
        )
        if comment:
            member.comment = comment
        if email:
            member.email = email
        
        member.clean()
        member.save()

        messages.success(request, 'You Info submitted, We will get in touch.')
        return redirect('home')
    
    messages.error(request, 'You Info Fail, Please try again.')
    return redirect('home')


def createQuestion(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        question = request.POST['question']
        gender = request.POST['gender']
        
        object = Question(
            question = question,
            gender=gender
        )
        if name:
            object.name = name
        if number:
            object.number = number

        
            
        object.clean()
        object.save()

        messages.success(request, 'You question submitted, We will reply. \nFind other question and answer on questions page')
        return redirect('home')
    
    messages.error(request, 'You Info Fail, Please try again.')
    return redirect('home')

#comment = BlogCategory.objects.get(pk=request.POST['category'])



def adminIndexView(request):

    question_wo = Question.objects.filter()

    return render(request, 'admin/index1.html')



class QuestionListView_(generic.ListView):
    queryset = Question.objects.all()
    model = Question
    paginate_by = 30
    context_object_name = 'objects'
    extra_context = {'year': datetime.now().year, 'title': 'Home', 'list': [1,2,3,4,5]}
    template_name = 'admin/question/question_list.html'

class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'admin/question/question_list.html'


class QuestionCreateView(generic.CreateView):
    model = Question
    template_name = 'admin/question/question_create.html'
    form_class = QuestionForm
    success_url = '/admin/question/'

class QuestionUpdateView(generic.UpdateView):
    model = Question
    template_name = 'admin/question/question_create.html'
    form_class = QuestionForm
    success_url = '/admin/question'

class QuestionDeleteView(generic.DeleteView):
    model = Question
    template_name = 'admin/question/question_create.html'
    success_url = '/admin/question/'

# Blog

class BlogListView_(generic.ListView):
    queryset = Blog.objects.all()
    model = Blog
    paginate_by = 30
    context_object_name = 'objects'
    extra_context = {'year': datetime.now().year, 'title': 'Home', 'list': [1,2,3,4,5]}
    template_name = 'admin/blog/blog_list.html'

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'admin/blog/blog_list.html'


class BlogCreateView(generic.CreateView):
    model = Blog
    template_name = 'admin/blog/blog_create.html'
    form_class = BlogForm
    success_url = '/admin/blog/'

class BlogUpdateView(generic.UpdateView):
    model = Blog
    template_name = 'admin/blog/blog_create.html'
    form_class = BlogForm
    success_url = '/admin/blog/'

class BlogDeleteView(generic.DeleteView):
    model = Blog
    template_name = 'admin/blog/blog_create.html'
    success_url = '/admin/blog/'


# Report

class ReportListView_(generic.ListView):
    queryset = Report.objects.all()
    model = Report
    paginate_by = 30
    context_object_name = 'objects'
    extra_context = {'year': datetime.now().year, 'title': 'Home', 'list': [1,2,3,4,5]}
    template_name = 'admin/report/report_list.html'

class ReportDetailView(generic.DetailView):
    model = Report
    template_name = 'admin/report/report_list.html'


class ReportCreateView(generic.CreateView):
    model = Report
    template_name = 'admin/report/report_create.html'
    form_class = ReportForm
    success_url = '/admin/report/'

class ReportUpdateView(generic.UpdateView):
    model = Report
    template_name = 'admin/report/report_update.html'
    form_class = ReportForm
    success_url = '/admin/report/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obb'] = Report.objects.get(pk=self.kwargs['pk']) 
        return context



class ReportDeleteView(generic.DeleteView):
    model = Report
    template_name = 'admin/report/report_create.html'
    success_url = '/admin/report/'


# Media

class MediaListView_(generic.ListView):
    queryset = Media.objects.all()
    model = Media
    paginate_by = 30
    context_object_name = 'objects'
    extra_context = {'year': datetime.now().year, 'title': 'Home', 'list': [1,2,3,4,5]}
    template_name = 'admin/media/media_list.html'

class MediaDetailView(generic.DetailView):
    model = Media
    template_name = 'admin/media/media_list.html'


class MediaCreateView(generic.CreateView):
    model = Media
    template_name = 'admin/media/media_create.html'
    form_class = MediaForm
    success_url = '/admin/media/'

class MediaUpdateView(generic.UpdateView):
    model = Media
    template_name = 'admin/media/media_create.html'
    form_class = MediaForm
    success_url = '/admin/media/'

class MediaDeleteView(generic.DeleteView):
    model = Media
    template_name = 'admin/media/media_create.html'
    success_url = '/admin/media/'



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have successful login')
            return redirect('ad_index')
        messages.error(request, 'email or password wrong')
        return redirect('login')
    return render(request, 'pages/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')


#download file 
def downloadReport(request, pk):
    obj = get_object_or_404(Report, pk=pk)
    file_path = obj.file.path
    response = FileResponse(open(file_path, 'rb'))
    obj.download_count += 1
    obj.save()
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{obj.name}.doc"'
    
    return response

