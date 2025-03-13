from django.contrib import admin

from .models import Departments, Doctors, Bookings

# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)


class BookingsAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'patient_name', 'doctor_name', 'patient_number', 'booking_date', 'booked_on')
                    


admin.site.register(Bookings, BookingsAdmin)   


