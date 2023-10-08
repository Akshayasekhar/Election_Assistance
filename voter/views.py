from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.db import IntegrityError

from officer.models import countofficer, CrowdUpdate
from .models import VoterSignup, Feedback
from commission.models import Person, OfficerAdd, Booth, Result
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'index.html')


def adminlog(request):
    return render(request, 'adminlog.html')

def service(request):
    return render(request, 'service.html')

def user(request):
    return render(request, 'user.html')

# def login_admin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         if user is not None:
#             auth.login(request, user)
#             return redirect('commission/logout')
#         else:
#             messages.info(request, 'Invalid Username or Password')
#             return redirect('login_admin')
#
#     else:
#
#      return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    booth_no = request.session.get('booth_no')
    booth = Booth.objects.filter(booth_no=booth_no).first()# Retrieve the booth details using booth_no from vuser
    people = Person.objects.filter(booth_no=booth_no).annotate(voter_count=Count('id'))
    voter_count = people.aggregate(total_count=Count('id'))['total_count']
    update = CrowdUpdate.objects.filter(booth_no=booth_no).order_by('-timestamp')
    latest_count = update.first().count if update else 0

    return render(request, 'count.html', {'booth': booth, 'booth_no': booth_no, 'voter_count': voter_count,'update': update,'latest_count': latest_count})



# def officer_login(request):
#   return render(request, 'officer_login.html')


def result(request):
    return render(request, 'result.html')
def demo(request):
    return render(request, 'demos.html')


# voter_register/views.py

from django.shortcuts import render, redirect
from .models import Voter
def register_voter(request):
    if request.method == 'POST':
        try:
            # Your existing code to extract form data and create a new Voter object
            name = request.POST['name']
            age = request.POST['age']
            house_no = request.POST['house_no']
            aadhar_id = request.POST['aadhar_id']
            gender = request.POST['gender']
            image = request.FILES.get('image')
            aadhar_file = request.FILES.get('aadhar_file')
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pin = request.POST['pin']
            email = request.POST['email']
            phone = request.POST['phone']

            # Create a new Voter object and save it to the database
            voter = Voter.objects.create(
                name=name,
                age=age,
                house_no=house_no,
                aadhar_id=aadhar_id,
                gender=gender,
                image=image,
                aadhar_file=aadhar_file,
                address=address,
                city=city,
                state=state,
                pin=pin,
                email=email,
                phone=phone
            )

            return redirect('voter_confirmation', voter_id=voter.id)

        except IntegrityError:
            error_message = f"A Person with Aadhar ID {aadhar_id} already Registered."
            return render(request, 'register_voter.html', {'error_message': error_message})

    return render(request, 'register_voter.html')




def voter_confirmation(request, voter_id):
    voter = get_object_or_404(Voter, id=voter_id)
    success_message = None

    if request.method == 'POST' and 'success' in request.GET:
        # This block will execute when the form is successfully submitted
        success_message = 'Registration Successful! Your details have been saved.'

    return render(request, 'voter_confirmation.html', {'voter': voter, 'success_message': success_message})

def submit_voter_details(request, voter_id):
    voter = get_object_or_404(Voter, id=voter_id)

    if request.method == 'POST':
        # # Update the voter details with the submitted form data
        # voter.name = request.POST.get('name')
        # voter.age = request.POST.get('age')
        # voter.house_no = request.POST.get('house_no')
        # voter.aadhar_id = request.POST.get('aadhar_id')
        # voter.gender = request.POST.get('gender')
        # voter.image = request.FILES.get['image']
        # voter.aadhar_file = request.FILES.get['aadhar_file']
        # voter.address = request.POST.get('address')
        # voter.city = request.POST.get('city')
        # voter.state = request.POST.get('state')
        # voter.pin = request.POST.get('pin')
        # voter.email = request.POST.get('email')
        # voter.phone = request.POST.get('phone')
        voter.confirmation = True

        # Add other fields as needed
        # Save the updated voter object
        voter.save()
        # Redirect to the voter_confirmation page with a success message
        return redirect('voter_confirmation', voter_id=voter_id)

    return redirect('voter_confirmation', voter_id=voter_id)


def edited_voter(request, voter_id):
    voter = get_object_or_404(Voter, id=voter_id)

    if request.method == 'POST':

            voter.name = request.POST.get('name')
            voter.age = request.POST.get('age')
            voter.house_no = request.POST.get('house_no')
            voter.aadhar_id = request.POST.get('aadhar_id')
            voter.gender = request.POST.get('gender')
            voter.image = request.FILES['image']
            voter.aadhar_file = request.FILES['aadhar_file']
            voter.address = request.POST.get('address')
            voter.city = request.POST.get('city')
            voter.state = request.POST.get('state')
            voter.pin = request.POST.get('pin')
            voter.email = request.POST.get('email')
            voter.phone = request.POST.get('phone')

    # Update other voter fields as needed
            voter.save()
            return redirect('voter_confirmation', voter_id=voter.id)

    return render(request, 'edited_voter.html', {'voter': voter})




def signup(request):
    if request.method == 'POST':
        v_name = request.POST['v_name']
        aadhar_id = request.POST['aadhar_id']
        # Check if Aadhar ID already exists
            # Check if Aadhar ID already exists
        if VoterSignup.objects.filter(aadhar_id=aadhar_id).exists():
                # Display error message
                messages.error(request, 'Aadhar ID already registered')
                return redirect('signup')

        try:
          date = request.POST['date']
          phone = request.POST['phone']
          gender = request.POST['gender']
          photo = request.FILES['photo']
          email = request.POST['email']
          vard_no = request.POST['vard_no']
          user = VoterSignup(v_name=v_name, aadhar_id=aadhar_id, date=date, phone=phone, gender=gender, photo=photo,email=email,vard_no=vard_no)
          user.save()
          messages.success(request, 'Registration successful')
          return redirect('signup')

        except IntegrityError:
          # Display user-friendly error message for duplicate entry
          messages.error(request, 'This Aadhar ID already registered.')
          return redirect('signup')
    return render(request, 'signup.html')


# views.py


# def slip(request):
#     aadhar_id = request.GET.get('aadhar_id')  # Get the selected ID from the request
#     vuser = get_object_or_404(Person, aadhar_id=aadhar_id)
#     booth = get_object_or_404(Booth, booth_no=vuser.booth_no)  # Retrieve the booth details using booth_no from vuser
#     return render(request, 'slip.html', {'vuser': vuser, 'booth': booth})

def slip(request):
    aadhar_id = request.GET.get('aadhar_id')  # Get the selected ID from the request

    try:
        vuser = Person.objects.get(aadhar_id=aadhar_id)
        booth = get_object_or_404(Booth, booth_no=vuser.booth_no)  # Retrieve the booth details using booth_no from vuser
        return render(request, 'slip.html', {'vuser': vuser, 'booth': booth})
    except Person.DoesNotExist:
        error_message = 'You are not enrolled in the voter list. Please make sure to enroll in the voter list.'
        return render(request, 'error.html', {'error_message': error_message})

def error(request):
        return render(request, 'error.html')


#def officer_login(request):
#    if request.method == 'POST':
#        booth_no = request.POST.get('booth_no')
#        email = request.POST.get('email')
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        # officer = authenticate(request, username=username, password=password)
#        user_exists = OfficerAdd.objects.filter(username=username, email=email,booth_no=booth_no).exists()

#        if user_exists:
          # User exists, perform login
#          officer = OfficerAdd.objects.get(username=username, email=email,booth_no=booth_no)

 #         if officer.password == password:
 #            return redirect('officer/verify_voter')

 #   return render(request, 'officer_login.html')




def officer_login(request):
    if request.method == 'POST':
        booth_no = request.POST.get('booth_no')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_exists = OfficerAdd.objects.filter(username=username, email=email, booth_no=booth_no).exists()

        if user_exists:
             officer = OfficerAdd.objects.get(username=username, email=email, booth_no=booth_no)
             if officer.password == password:
                request.session['booth_no'] = booth_no

                # Pass officer's first name to the template context
                return render(request, 'verify_voter.html', {'fname': officer.fname, 'sname': officer.sname })

             # return redirect('officer/verify_voter', fname=OfficerAdd.fname)
             # Invalid details, display an error message
        messages.error(request, 'Invalid login details.')

    return render(request, 'officer_login.html')


def c_officer_login(request):
    if request.method == 'POST':
        booth_no = request.POST.get('booth_no')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # officer = authenticate(request, username=username, password=password)
        user_exists = countofficer.objects.filter(username=username, email=email,booth_no=booth_no).exists()

        if user_exists:
          # User exists, perform login
          c_officer = countofficer.objects.get(username=username, email=email,booth_no=booth_no)

          if c_officer.password == password:
              request.session['booth_no'] = booth_no

              return redirect('officer/update_count')

        messages.error(request, 'Invalid login details.')

    return render(request, 'c_officer_login.html')


def result(request):
    results = Result.objects.all()
    search_query = request.GET.get('constituency_search')
    if search_query:
        # If there's a search query, filter the results based on the constituency name
        results = Result.objects.filter(constituency__icontains=search_query)
    print("Search Query:", search_query)
    print("Filtered Results Count:", results.count())

    return render(request, 'result.html', {'results': results})

def enter_booth(request):
    if request.method == 'POST':
        booth_no = request.POST.get('booth_no')
        request.session['booth_no'] = booth_no
        return redirect('count')
    return render(request, 'enter_booth.html')


def feedback_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the feedback to the database
        feedback = Feedback.objects.create(name=name, email=email, message=message)
        feedback.save()
        messages.success(request, 'Thank you for your feedback! We appreciate your input.')
    return render(request, 'index.html')

