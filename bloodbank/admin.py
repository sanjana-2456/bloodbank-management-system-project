
from django.contrib import admin
from .models import Donor, Donation, BloodStock, BloodRequest
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name','blood_group','phone','last_donation')
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor','date','units')
@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):
    list_display = ('blood_group','units_available')
@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('patient_name','blood_group','units_required','fulfilled')
