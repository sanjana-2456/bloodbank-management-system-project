
from django.db import models
from django.utils import timezone
BLOOD_GROUPS = [
    ('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),
    ('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-'),
]
class Donor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    last_donation = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    def __str__(self):
        return f"{self.name} ({self.blood_group})"
class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='donations')
    date = models.DateField(default=timezone.now)
    units = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)
    def __str__(self):
        return f"Donation {self.donor.name} on {self.date} - {self.units} unit(s)"
class BloodStock(models.Model):
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, unique=True)
    units_available = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.blood_group}: {self.units_available} unit(s)"
class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=200)
    hospital = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units_required = models.PositiveIntegerField()
    requested_on = models.DateTimeField(default=timezone.now)
    fulfilled = models.BooleanField(default=False)
    def __str__(self):
        return f"Request {self.patient_name} - {self.blood_group} ({self.units_required})"
