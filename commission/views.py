from functools import wraps

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from voter.models import VoterSignup, Voter, Feedback

from django.contrib.auth import logout

from commission.models import OfficerAdd, Person, Booth, Result, VoterRegistration
from itertools import groupby
from operator import attrgetter

# Create your views here.

#def index(request):
#    return render(request, 'index.html')

def logout_admin(request):
    logout(request)
    return redirect('index')  # Replace 'home' with the name of the URL pattern for your home page



def registered_people(request):
    people = VoterSignup.objects.order_by('vard_no')
    grouped_people = []
    for vard_no, group in groupby(people, key=lambda x: x.vard_no):
        grouped_people.append((vard_no, list(group)))
    return render(request, 'registered_people.html', {'grouped_people': grouped_people})
def addofficer(request):
    return render(request, 'addofficer.html')

def publishresult(request):
    return render(request, 'publish_result.html')



def adminhome(request):
    return render(request, 'adminhome.html')



def addofficer(request):
    error_message = None

    if request.method == 'POST':

        try:

          fname = request.POST['fname']
          sname = request.POST['sname']
          address = request.POST['address']
          radio = request.POST['radio']
          phone = request.POST['phone']
          booth_no = request.POST['booth_no']
          email = request.POST['email']
          username = request.POST['username']
          password = request.POST['password']

          user = OfficerAdd(fname=fname, sname=sname, address=address, radio=radio, phone=phone, booth_no=booth_no, email=email, username=username, password=password)
          user.save()
          return redirect('officer_details')  # Redirect to the list view
        except IntegrityError:
            error_message = "Username already exists."


    return render(request, 'addofficer.html', {'error_message': error_message})


# def officer_details(request):
#    people = OfficerAdd.objects.all()
#    return render(request, 'officer_details.html', {'people': people})

# views.py

from django.db import IntegrityError

def add(request):
    if request.method == 'POST':
        try:


                    voter_id = request.POST['voter_id']
                    name = request.POST['name']
                    aadhar_id = request.POST['aadhar_id']
                    house_no = request.POST['house_no']
                    age = request.POST['age']
                    gender = request.POST['gender']
                    image = request.FILES['image']
                    if VoterRegistration.objects.filter(voter_id=voter_id).exists():
                        messages.error(request, 'Voter ID already registered')
                    else:
                        user = VoterRegistration(voter_id=voter_id, name=name, aadhar_id=aadhar_id, house_no=house_no, age=age, gender=gender, image=image)
                        user.save()
                        success_message = "Registration successful!"  # Add the success message here
                        return render(request, 'add.html', {'success_message': success_message})
        except IntegrityError:
                error_message = f"A Person with Aadhar ID {aadhar_id} already exists."
                return render(request, 'add.html', {'error_message': error_message})

    return render(request,'add.html')



def admin_view(request):
    voters = VoterRegistration.objects.all()
    return render(request, 'admin_view.html', {'voters': voters})


from django.shortcuts import render, redirect
from .models import VoterRegistration, Person

def add_to_person_table(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        voter_id = request.POST.get('voter_id')
        if action == 'approve':

          booth_no = request.POST.get('booth_no')
          # Check if the booth number exists in the Booth table
          if not Booth.objects.filter(booth_no=booth_no).exists():
              messages.error(request, f"Booth Number {booth_no} does not exist.")
              return redirect('admin_view')
          try:
            # Retrieve the corresponding voter registration record
            voter_registration = VoterRegistration.objects.get(voter_id=voter_id)

            # Create a corresponding Person entry
            person = Person.objects.create(
                voter_id=voter_registration.voter_id,
                name=voter_registration.name,
                aadhar_id=voter_registration.aadhar_id,
                house_no=voter_registration.house_no,
                age=voter_registration.age,
                gender=voter_registration.gender,
                image=voter_registration.image,
                booth_no=booth_no,  # Add the appropriate booth number here
                verified=False
            )
            # Save the person instance
            person.save()

            # Delete the VoterRegistration record
            voter_registration.delete()
            return redirect('admin_view')  # Redirect to admin view page after processing

          except IntegrityError:
             error_message = f"A Person with Voter ID {voter_id} already exists."
             voters = VoterRegistration.objects.all()
             return render(request, 'admin_view.html', {'error_message': error_message,'voters': voters})
        elif action == 'reject':
              # Retrieve the corresponding voter registration record and delete it
              voter_registration = VoterRegistration.objects.get(voter_id=voter_id)
              voter_registration.delete()

              # Redirect back to the admin view page after rejecting
              return redirect('admin_view')
    return redirect('admin_view')


from django.contrib import messages


def add_to_person(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        v_id = request.POST.get('v_id')
        if action == 'approve':
            booth_no = request.POST.get('booth_no')
            # Check if the booth number exists in the Booth table
            if not Booth.objects.filter(booth_no=booth_no).exists():
                messages.error(request, f"Booth Number {booth_no} does not exist.")
                return redirect('enrollment')
            else:

              voter_id = request.POST.get('voter_id')
              if Person.objects.filter(voter_id=voter_id).exists():
                messages.error(request, 'Voter ID already registered')
              else:
                # Retrieve the corresponding voter registration record
                    try:
                      voter = Voter.objects.get(pk=v_id)

                    # Create a corresponding Person entry
                      person = Person.objects.create(
                        voter_id=voter_id,
                        name=voter.name,
                        aadhar_id=voter.aadhar_id,
                        house_no=voter.house_no,
                        age=voter.age,
                        gender=voter.gender,
                        image=voter.image,
                        booth_no=booth_no,  # Add the appropriate booth number here
                        verified=False
                      )
                      # Save the person instance
                      person.save()
                      voter.delete()
                      messages.success(request, 'Voter approved successfully!')
                    except IntegrityError:
                      # Display user-friendly error message for duplicate entry
                      messages.error(request, 'This Aadhar ID already registered.')
        elif action == 'reject':
              # Retrieve the corresponding voter registration record and delete it
              voter = Voter.objects.get(pk=v_id)
              voter.delete()
              messages.success(request, 'Voter rejected successfully!')

        return redirect('enrollment')

    return redirect('enrollment')
#
# def add_to_person(request):
#     if request.method == 'POST':
#       action = request.POST.get('action')
#
#       v_id = request.POST.get('v_id')
#       if action == 'approve':
#
#         booth_no = request.POST.get('booth_no')
#         voter_id = request.POST.get('voter_id')
#         if Person.objects.filter(voter_id=voter_id).exists():
#             messages.error(request, 'Voter ID already registered')
#             return redirect('enrollment')
#
#         else:    # Retrieve the corresponding voter registration record
#             voter = Voter.objects.get(pk=v_id)
#             try:
#
#               # Create a corresponding Person entry
#               person = Person.objects.create(
#                 voter_id=voter_id,
#                 name=voter.name,
#                 aadhar_id=voter.aadhar_id,
#                 house_no=voter.house_no,
#                 age=voter.age,
#                 gender=voter.gender,
#                 image=voter.image,
#                 booth_no=booth_no,  # Add the appropriate booth number here
#                 verified=False
#               )
#               # Save the person instance
#               person.save()
#
#               # Delete the VoterRegistration record
#               return redirect('enrollment')  # Redirect to admin view page after processing
#             except IntegrityError:
#              # Display user-friendly error message for duplicate entry
#               messages.error(request, 'This Aadhar ID already registered.')
#               return redirect('enrollment')
#       elif action == 'reject':
#         # Retrieve the corresponding voter registration record and delete it




from django.shortcuts import render
from django.db.models import Count
from itertools import groupby
from operator import attrgetter
#
def voterlist(request):
    grouped_people = Person.objects.values('booth_no').annotate(voter_count=Count('id')).order_by('booth_no')

    for group in grouped_people:
        group['people'] = Person.objects.filter(booth_no=group['booth_no'])

    return render(request, 'voterlist.html', {'grouped_people': grouped_people})

def officer_details(request):
    officer = OfficerAdd.objects.all()
    return render(request, 'officer_details.html', {'officer': officer})



def add_booth_details(request):
    if request.method == 'POST':
        try:
            booth_no = request.POST['booth_no']
            location = request.POST['location']
            user = Booth(booth_no=booth_no, location=location)
            user.save()
            messages.success(request, f'Polling Booth Number {booth_no} added successfully!')

            return render(request, 'add_booth_details.html')

        except IntegrityError:
         # Display user-friendly error message for duplicate entry
         messages.error(request, 'This Booth Details  already Added.')
    return render(request, 'add_booth_details.html')


def booth_details(request):
    booths = Booth.objects.all()
    return render(request, 'booth_details.html',{'booths': booths})



def publish_result(request):
    if request.method == 'POST':
      try:

        constituency = request.POST['constituency']
        c_name = request.POST['c_name']
        party_name = request.POST['party_name']
        vote_count = request.POST['vote_count']
        percentage = request.POST['percentage']
        photo = request.FILES['photo']
        user = Result(constituency=constituency, c_name=c_name, party_name=party_name,vote_count=vote_count,percentage=percentage,photo=photo)
        user.save()
        messages.success(request, f'Result for {constituency} published successfully!')
        return redirect('publish_result')
      except IntegrityError:
          # Display user-friendly error message for duplicate entry
          messages.error(request, 'This constituency already entered.')

    return render(request, 'publish_result.html')


from django.shortcuts import render, redirect
from .models import VoterSignup


# views.py
from django.shortcuts import render, redirect
from .models import Person

def edit_voter(request, voter_id):
    voter = Person.objects.get(id=voter_id)

    if request.method == 'POST':
        voter.name = request.POST.get('name')
        voter.aadhar_id = request.POST.get('aadhar_id')
        voter.voter_id = request.POST.get('voter_id')
        voter.house_no = request.POST.get('house_no')
        voter.age = request.POST.get('age')
        voter.gender = request.POST.get('gender')
        voter.image = request.FILES['image']
        voter.booth_no = request.POST.get('booth_no')

        # Update other voter fields as needed
        voter.save()
        return redirect('voterlist')  # Redirect to the voter list page after successful editing

    return render(request, 'edit_voter.html', {'voter': voter})


def edit_officer(request, username):
    officer = OfficerAdd.objects.get(username=username)
    error_message = None

    if request.method == 'POST':
        try:
            # Check if the new username is different from the current one
            if officer.username != username:
                OfficerAdd.objects.get(username=username)  # Check if the new username already exists

                error_message = "Username already exists."
            else:
               officer.fname = request.POST.get('fname')
               officer.sname = request.POST.get('sname')
               officer.address = request.POST.get('address')
               officer.radio = request.POST.get('radio')
               officer.phone = request.POST.get('phone')
               officer.booth_no = request.POST.get('booth_no')
               officer.email = request.POST.get('email')
               officer.username = request.POST.get('username')
               officer.password = request.POST.get('password')

               # Update other voter fields as needed
               officer.save()
               return redirect('officer_details')  # Redirect to the voter list page after successful editing
        except IntegrityError:
            error_message = "Username already exists."

    return render(request, 'edit_officer.html', {'officer': officer, 'error_message': error_message})


def remove_voter(request, voter_id):
    voter = Person.objects.get(id=voter_id)

    if request.method == 'POST':
        voter.delete()
        return redirect('voterlist')  # Redirect to the voter list page after successful removal

    return render(request, 'remove_voter.html', {'voter': voter})



def remove_officer(request, username):
    officer = OfficerAdd.objects.get(username=username)

    if request.method == 'POST':
        officer.delete()
        return redirect('officer_details')  # Redirect to the voter list page after successful removal

    return render(request, 'remove_officer.html', {'officer': officer})


def enrollment(request):
    confirmed_voters = Voter.objects.filter(confirmation=True)
    return render(request, 'enrollment.html', {'result_list': confirmed_voters})



def officer_feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'officer_feedback.html', {'feedbacks': feedbacks})