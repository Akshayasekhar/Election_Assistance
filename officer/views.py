from functools import wraps

from django.core.checks import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import countofficer, CrowdUpdate
from django.contrib.auth.models import User, auth
from commission.models import Person, OfficerAdd

from itertools import groupby
from operator import attrgetter
#from officer.models import countofficer

# Create your views here.
# def login_required_customs(view_func):
#     @wraps(view_func)
#     def wrapped_view(request, *args, **kwargs):
#         if not request.session.get('username'):
#             return redirect('officer_login')  # Redirect to the login page
#         return view_func(request, *args, **kwargs)
#     return wrapped_view
#
# def login_required_customss(view_func):
#     @wraps(view_func)
#     def wrapped_view(request, *args, **kwargs):
#         if not request.session.get('username'):
#             return redirect('c_officer_login')  # Redirect to the login page
#         return view_func(request, *args, **kwargs)
#     return wrapped_view

def logout_officer(request):
    logout(request)
    return redirect('index')

    # Replace 'home' with the name of the URL pattern for your home page

def logout_c_officer(request):
    logout(request)
    return redirect('index')

#def index(request):
#   return render(request, 'index.html')

def guide_registration(request):
    return render(request, 'guide_registration.html')


from django.contrib import messages
def counting_officer(request):
    if request.method == 'POST':
      try:
        booth_no = request.session.get('booth_no')

        # booth_no = request.POST['booth_no']
        name = request.POST['name']
        address = request.POST['address']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = countofficer(booth_no=booth_no, name=name, address=address, gender=gender,phone=phone,email=email,username=username,password=password)
        user.save()
        return redirect('counting_officer_details')  # Replace 'home' with the name of the URL pattern for your home page
      except IntegrityError:
          # Display user-friendly error message for duplicate entry
          messages.error(request, 'This username already registered.')

    return render(request, 'counting_officer.html')


def verify_voter(request):
    return render(request, 'verify_voter.html')
# def update_count(request):
#     return render(request, 'update_count.html')


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_count(request):
    if request.method == 'POST':
        booth_no = request.session.get('booth_no')
        crowd_count = request.POST.get('crowd_count')
        percentage = request.POST.get('percentage')
        # Save the crowd count update to the database
        CrowdUpdate.objects.create(booth_no=booth_no, count=crowd_count, percentage=percentage)

    booth_no = request.session.get('booth_no')  # Retrieve booth_no from the session
    # Retrieve all crowd count updates from the database
    update = CrowdUpdate.objects.filter(booth_no=booth_no).order_by('-timestamp')
    latest_count = update.first().count if update else 0

    return render(request, 'update_count.html', {'update': update,'latest_count': latest_count})


def counting_officer_details(request):
    booth_no = request.session.get('booth_no')
    c_officer = countofficer.objects.filter(booth_no=booth_no)
    return render(request, 'counting_officer_details.html', {'c_officer': c_officer})



# def counting_officer_details(request):
#     c_officer = countofficer.objects.all()
#     return render(request, 'counting_officer_details.html', {'c_officer': c_officer})

# def show_voter(request):
#     booth_no = request.session.get('booth_no')
#     people = Person.objects.filter(booth_no=booth_no)
#     return render(request, 'show_voter.html', {'people': people})
from django.db.models import Count
#
# def show_voter(request):
#     booth_no = request.session.get('booth_no')
#     people = Person.objects.filter(booth_no=booth_no).annotate(voter_count=Count('id'))
#     return render(request, 'show_voter.html', {'people': people})
from django.db.models import Count
def show_voter(request):
    booth_no = request.session.get('booth_no')
    people = Person.objects.filter(booth_no=booth_no).annotate(voter_count=Count('id'))
    voter_count = people.aggregate(total_count=Count('id'))['total_count']
    return render(request, 'show_voter.html', {'people': people, 'booth_no': booth_no, 'voter_count': voter_count})
