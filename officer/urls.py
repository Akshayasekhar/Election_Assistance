from django.urls import path
from . import views
from .views import logout_officer, logout_c_officer

urlpatterns = [
   # path('', views.index, name='index'),
    path('guide_registration', views.guide_registration, name='guide_registration'),
    path('verify_voter', views.verify_voter, name='verify_voter'),
    path('show_voter', views.show_voter, name='show_voter'),
    path('logout_officer/', logout_officer, name='logout_officer'),
    path('logout_c_officer/', logout_c_officer, name='logout_c_officer'),

    path('counting_officer', views.counting_officer, name='counting_officer'),
    path('update_count', views.update_count, name='update_count'),

    path('counting_officer_details', views.counting_officer_details, name='counting_officer_details'),

]
