from django.urls import path
from . import views

urlpatterns = [
    #path('success', views.success, name='success'),
    # path('recognize_faces', views.recognize_faces, name='recognize_faces'),
   # path('trueface', views.trueface, name='trueface'),
    path('verify_person_view', views.verify_person_view, name='verify_person_view'),
    path('verify_person', views.verify_person_view, name='verify_person'),

]