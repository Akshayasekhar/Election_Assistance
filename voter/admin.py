from django.contrib import admin


from .models import VoterSignup
# Register your models here.


class VoterDetails(admin.ModelAdmin):
    list_display = ('v_name', 'aadhar_id', 'date', 'phone', 'gender', 'photo')


admin.site.register(VoterSignup, VoterDetails)

from .models import Feedback

admin.site.register(Feedback)