from django import forms

from .models import Bookings


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'
        
        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'patient_name': "patient Name ",
            'doctor_name': "Doctor Name ",
            'department_name': "Department Name ",
            'booking_date': "Booking Date ",
           
            
        }


        