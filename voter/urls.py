from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('count', views.count, name='count'),
    path('officer_login', views.officer_login, name='officer_login'),
    path('result', views.result, name='result'),
    path('signup', views.signup, name='signup'),
    path('slip', views.slip, name='slip'),
    path('user', views.user, name='user'),
    path('demo', views.demo, name='demo'),
    path('c_officer_login', views.c_officer_login, name='c_officer_login'),
    path('error', views.error, name='error'),
    path('enter_booth', views.enter_booth, name='enter_booth'),
    path('service', views.service, name='service'),
    path('adminlog', views.adminlog, name='adminlog'),
    path('register_voter/', views.register_voter, name='register_voter'),
    path('confirmation/<int:voter_id>/', views.voter_confirmation, name='voter_confirmation'),
    path('edited_voter/<int:voter_id>/', views.edited_voter, name='edited_voter'),
    path('voter_confirmation/<int:voter_id>/submit/', views.submit_voter_details, name='submit_voter_details'),
    path('feedback/', views.feedback_form, name='feedback_form'),

]
