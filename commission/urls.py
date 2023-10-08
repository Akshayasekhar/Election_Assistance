from django.urls import path
from .import views
from .views import logout_admin

urlpatterns = [
   # path('index', views.index, name='index'),
    path('voterlist', views.voterlist, name='voterlist'),
    path('registered_people', views.registered_people, name='registered_people'),
    path('addofficer', views.addofficer, name='addofficer'),
    path('publish_result', views.publish_result, name='publish_result'),
    path('logout_admin/', logout_admin, name='logout_admin'),
    path('add', views.add, name='add'),
    path('edit_voter/<int:voter_id>/', views.edit_voter, name='edit_voter'),
    path('remove_voter/<int:voter_id>/', views.remove_voter, name='remove_voter'),
    path('edit_officer/<str:username>/', views.edit_officer, name='edit_officer'),
    path('remove_officer/<str:username>/', views.remove_officer, name='remove_officer'),
    # path('approve_registration/<int:registration_id>/', views.approve_registration, name='approve_registration'),
    path('enrollment/', views.enrollment, name='enrollment'),

    path('voterlist/<int:voter_id>/', views.voterlist, name='voterlist'),
    path('officer_details', views.officer_details, name='officer_details'),
    path('add_booth_details', views.add_booth_details, name='add_booth_details'),
    path('booth_details', views.booth_details, name='booth_details'),
    path('adminhome', views.adminhome, name='adminhome'),

    # Other URL patterns...
    path('admin_view/', views.admin_view, name='admin_view'),
    path('add_to_person_table/', views.add_to_person_table, name='add_to_person_table'),
    path('add_to_person/', views.add_to_person, name='add_to_person'),
    path('officer_feedback/', views.officer_feedback, name='officer_feedback'),

]
