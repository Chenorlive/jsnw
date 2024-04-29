from django.urls import path
from .views import (
    index, about, createMember, createQuestion,
    BlogListView, QuestionListView, ReportListView,
    login_view, logout_view, aboutDistrict, FAQListView,
    gallery, adminIndexView, QuestionCreateView, QuestionUpdateView,
    QuestionListView_, QuestionDetailView, contact, 
    BlogListView_, BlogDetailView, BlogUpdateView, BlogCreateView,
    ReportListView_, ReportCreateView, ReportDetailView, ReportUpdateView,
    MediaListView_, MediaCreateView, MediaDetailView, MediaUpdateView,
    downloadReport
)


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('question/', QuestionListView.as_view(), name='question'),
    path('faq/', FAQListView.as_view(), name='faq'),
    path('report/', ReportListView.as_view(), name='report'),
    path('about/district', aboutDistrict, name='about_dis'),
    path('gallery', gallery, name='gallery'),


    path('member/new', createMember, name='new_member'),
    path('question/new', createQuestion, name='new_question'),


    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    #admin
     path('admin/', adminIndexView, name='ad_index'),

    path('admin/question/', QuestionListView_.as_view(), name='ad_list_question'),
    path('admin/question/<int:pk>/', QuestionDetailView.as_view(), name='ad_detail_question'),
    path('admin/question/new/', QuestionCreateView.as_view(), name='ad_new_question'),
    path('admin/question/update/<pk>/', QuestionUpdateView.as_view(), name='ad_update_question'),

    path('admin/blog/', BlogListView_.as_view(), name='ad_list_blog'),
    path('admin/blog/<int:pk>/', BlogDetailView.as_view(), name='ad_detail_blog'),
    path('admin/blog/new/', BlogCreateView.as_view(), name='ad_new_blog'),
    path('admin/blog/update/<int:pk>/', BlogUpdateView.as_view(), name='ad_update_blog'),

    path('admin/report/', ReportListView_.as_view(), name='ad_list_report'),
    path('admin/report/<int:pk>/', ReportDetailView.as_view(), name='ad_detail_report'),
    path('admin/report/', ReportCreateView.as_view(), name='ad_new_report'),
    path('admin/report/update/<int:pk>/', ReportUpdateView.as_view(), name='ad_update_report'),

    path('admin/media/', MediaListView_.as_view(), name='ad_list_media'),
    path('admin/media/<int:pk>/', MediaDetailView.as_view(), name='ad_detail_media'),
    path('admin/media/new/', MediaCreateView.as_view(), name='ad_new_media'),
    path('admin/media/update/<int:pk>/', MediaUpdateView.as_view(), name='ad_update_media'),

    path('download/report/<int:pk>/', downloadReport, name="download_report")
]