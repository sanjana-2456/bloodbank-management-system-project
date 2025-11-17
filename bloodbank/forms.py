
from django import forms
from .models import Donor, BloodRequest
class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name','email','phone','blood_group','last_donation','address']
class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['patient_name','hospital','blood_group','units_required']
