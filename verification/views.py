#
# from django.shortcuts import render
#
# # Create your views here.
# import base64
# from pathlib import Path
# from PIL import Image
# from django.core.checks import messages
# from django.core.files import images
# from django.shortcuts import get_object_or_404, redirect, render
# import numpy as np
#
# import face_recognition
# from commission.models import Person
# from smartvote import settings
# from django.contrib import messages
#
#
# # ... import statements ...
# import cv2
# import face_recognition
# from django.shortcuts import get_object_or_404
# from commission.models import Person
# from django.contrib.messages import add_message
# #
# # def verify_person(request, voter_id, captured_image):
# #     # Get the person object from the database using the provided voter_id
# #     # person = get_object_or_404(Person, voter_id=voter_id)
# #     # Get the person object from the database using the provided voter_id
# #     # person = Person.objects.filter(voter_id=voter_id).first()
# #     # Get the person object from the database using the provided voter_id and booth number
# #     person = Person.objects.filter(voter_id=voter_id, booth_no=request.session.get('booth_no')).first()
# #
# #     if person is None:
# #         # Voter ID not found in the voter list
# #         messages.error(request, 'Invalid voter ID. Voter not found in the voter list.')
# #         return None
# #
# #     # Load the stored image from the database
# #     stored_image = face_recognition.load_image_file(person.image.path)
# #
# #     # Encode the faces in the stored image
# #     stored_face_encodings = face_recognition.face_encodings(stored_image)
# #
# #     # Load the captured image
# #     captured_image = face_recognition.load_image_file(captured_image)
# #
# #     # Find faces in the captured image
# #     captured_face_encodings = face_recognition.face_encodings(captured_image)
# #
# #     # Compare the captured face encodings with the stored face encodings
# #     for captured_encoding in captured_face_encodings:
# #         matches = face_recognition.compare_faces(stored_face_encodings, captured_encoding)
# #         if True in matches:
# #             # Images match, return the person details
# #             if person.verified:
# #                 # Person has already been verified (already voted)
# #                 messages.warning(request, 'This person has already voted.')
# #             else:
# #                 person.verified = True  # Update the 'verified' field to True
# #                 person.save()  # Save the changes to the database
# #                 return person  # Return the person object if verification is successful
# #
# #
# #         else:
# #             messages.error(request, 'Image does not match the stored record.')
# #
# #               # Images do not match
# #             return None
# # #
# # def verify_person(request, voter_id, captured_image):
# #     # Get the person object from the database using the provided voter_id and booth number
# #     person = Person.objects.filter(voter_id=voter_id, booth_no=request.session.get('booth_no')).first()
# #
# #     if person is None:
# #         # Voter ID not found in the voter list
# #         messages.error(request, 'Invalid voter ID. Voter not found in the voter list.')
# #         return None
# #
# #     # Load the stored image from the database
# #     stored_image = face_recognition.load_image_file(person.image.path)
# #
# #     # Encode the face in the stored image
# #     stored_face_encoding = face_recognition.face_encodings(stored_image)
# #
# #     # Load the captured image
# #     captured_image = face_recognition.load_image_file(captured_image)
# #
# #     # Find faces in the captured image
# #     captured_face_encodings = face_recognition.face_encodings(captured_image)
# #
# #     # Compare the captured face encodings with the stored face encoding
# #     if len(captured_face_encodings) > 0:
# #         captured_encoding = captured_face_encodings[0]
# #         match = face_recognition.compare_faces(stored_face_encoding, captured_encoding)[0]
# #
# #         if match:
# #             # Images match, return the person details
# #             if person.verified:
# #                 # Person has already been verified (already voted)
# #                 messages.warning(request, 'This person has already voted.')
# #             else:
# #                 person.verified = True  # Update the 'verified' field to True
# #                 person.save()  # Save the changes to the database
# #                 messages.success(request, 'Verification successful! You may proceed.')
# #                 return person  # Return the person object if verification is successful
# #         else:
# #             messages.error(request, 'Image does not match the stored record.')
# #
# #     else:
# #         messages.error(request, 'No face found in the uploaded image.')
# #
# #     # Images do not match or no face found
# #     return None
# #
# #
# #
# # from django.shortcuts import render
# # from commission.models import Person
# # # from .utils import verify_person
# #
# #
# # def verify_person_view(request):
# #     if request.method == 'POST':
# #         voter_id = request.POST.get('voter_id')
# #         captured_image = request.FILES.get('image')
# #
# #         person = verify_person(request, voter_id, captured_image)
# #
# #         if person is not None:
# #             # Verification successful
# #             context = {'person': person}
# #             return render(request, 'success.html', context)
# #
# #     return render(request, 'verify_person_view.html')
# #
# import face_recognition
# from django.shortcuts import render
# from django.contrib import messages
# from commission.models import Person
#
# def verify_person(request, v_id, captured_image):
#     # Get the person object from the database using the provided voter_id and booth number
#     person = Person.objects.filter(voter_id=v_id, booth_no=request.session.get('booth_no')).first()
#
#     if person is None:
#         # Voter ID not found in the voter list
#         messages.error(request, 'Invalid voter ID. Voter not found in the voter list.')
#         return None
#     # Load the captured image
#     captured_image = face_recognition.load_image_file(captured_image)
#
#     # Find faces in the captured image
#     captured_face_encodings = face_recognition.face_encodings(captured_image)
#
#     if len(captured_face_encodings) == 0:
#         messages.error(request, 'No face found in the captured image.')
#         return None
#
#     # Compare the captured face encoding with the stored face encoding only if voter_id matches
#     if person.voter_id == v_id:
#         # Load the stored image from the database
#         stored_image = face_recognition.load_image_file(person.image.path)
#
#         # Encode the face in the stored image
#         stored_face_encoding = face_recognition.face_encodings(stored_image)
#
#         if len(stored_face_encoding) == 0:
#             messages.error(request, 'No face found in the stored image.')
#             return None
#
#         captured_encoding = captured_face_encodings[0]
#         match = face_recognition.compare_faces(stored_face_encoding, captured_encoding, tolerance=0.4)[0]
#
#         # if any(matches):
#
#         if match:
#             # Images match, return the person details
#             if person.verified:
#                 # Person has already been verified (already voted)
#                 messages.warning(request, 'This person has already voted.')
#             else:
#                 person.verified = True  # Update the 'verified' field to True
#                 person.save()  # Save the changes to the database
#                 # messages.success(request, 'Verification successful! You may proceed.')
#                 return person  # Return the person object if verification is successful
#         else:
#             messages.error(request, 'Image does not match the stored record.')
#         return None
#
#
#
# def verify_person_view(request):
#     if request.method == 'POST':
#         v_id = request.POST.get('v_id')
#         captured_image = request.FILES.get('image')
#
#         person = verify_person(request, v_id, captured_image)
#
#         if person is not None:
#             # Verification successful
#             context = {'person': person}
#             return render(request, 'success.html', context)
#
#     return render(request, 'verify_person_view.html')
import face_recognition
from django.shortcuts import render
from django.contrib import messages
from commission.models import Person

def verify_person(request, voter_id, captured_image):
    # Get the person object from the database using the provided voter_id and booth number
    person = Person.objects.filter(voter_id=voter_id, booth_no=request.session.get('booth_no')).first()

    if person is None:
        # Voter ID not found in the voter list
        messages.error(request, 'Invalid voter ID. Voter not found in the voter list.')
        return None

    # Load the stored image from the database
    stored_image = face_recognition.load_image_file(person.image.path)

    # Encode the face in the stored image
    stored_face_encoding = face_recognition.face_encodings(stored_image)

    # Load the captured image
    captured_image = face_recognition.load_image_file(captured_image)

    # Find faces in the captured image
    captured_face_encodings = face_recognition.face_encodings(captured_image)

    if len(captured_face_encodings) == 0:
        messages.error(request, 'No face found in the captured image.')
        return None

    captured_encoding = captured_face_encodings[0]
    match = face_recognition.compare_faces(stored_face_encoding, captured_encoding, tolerance=0.5)[0]

    if match:
        # Images match, return the person details
        if person.verified:
            # Person has already been verified (already voted)
            messages.warning(request, 'This person has already voted.')
        else:
            person.verified = True  # Update the 'verified' field to True
            person.save()  # Save the changes to the database
            # messages.success(request, 'Verification successful! You may proceed.')
            return person  # Return the person object if verification is successful
    else:
        messages.error(request, 'Image does not match the stored record.')
    return None

def verify_person_view(request):
    if request.method == 'POST':
        voter_id = request.POST.get('voter_id')
        captured_image = request.FILES.get('image')

        person = verify_person(request, voter_id, captured_image)

        if person is not None:
            # Verification successful
            context = {'person': person}
            return render(request, 'success.html', context)

    return render(request, 'verify_person_view.html')
