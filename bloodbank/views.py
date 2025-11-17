from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import Donor, BloodStock, BloodRequest, Donation
from .forms import DonorForm, BloodRequestForm


# ------------------- Home Page -------------------
def index(request):
    stocks = BloodStock.objects.all().order_by('blood_group')
    recent_donors = Donor.objects.order_by('-last_donation')[:5]
    requests = BloodRequest.objects.filter(fulfilled=False).order_by('-requested_on')[:5]
    return render(request, 'bloodbank/index.html', {
        'stocks': stocks,
        'recent_donors': recent_donors,
        'requests': requests
    })


# ------------------- Donors -------------------
def donors_list(request):
    donors = Donor.objects.all().order_by('name')
    return render(request, 'bloodbank/donors_list.html', {'donors': donors})


def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Donor added successfully.")
            return redirect('donors_list')
    else:
        form = DonorForm()
    return render(request, 'bloodbank/add_donor.html', {'form': form})


def stock_update_from_donation(donor_id, units=1):
    donor = Donor.objects.get(pk=donor_id)
    stock, _ = BloodStock.objects.get_or_create(blood_group=donor.blood_group)
    stock.units_available += units
    stock.save()


def record_donation(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    if request.method == 'POST':
        units = int(request.POST.get('units', 1))
        Donation.objects.create(donor=donor, units=units)
        stock, _ = BloodStock.objects.get_or_create(blood_group=donor.blood_group)
        stock.units_available += units
        stock.save()
        donor.last_donation = Donation.objects.latest('date').date
        donor.save()
        messages.success(request, "Donation recorded successfully.")
        return redirect('donors_list')
    return render(request, 'bloodbank/record_donation.html', {'donor': donor})


# ------------------- Requests -------------------
def requests_list(request):
    reqs = BloodRequest.objects.all().order_by('-requested_on')
    return render(request, 'bloodbank/requests_list.html', {'requests': reqs})


def add_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Blood request added successfully.")
            return redirect('requests_list')
    else:
        form = BloodRequestForm()
    return render(request, 'bloodbank/add_request.html', {'form': form})


def fulfill_request(request, request_id):
    req = get_object_or_404(BloodRequest, pk=request_id)
    stock = BloodStock.objects.filter(blood_group=req.blood_group).first()
    if stock and stock.units_available >= req.units_required:
        stock.units_available -= req.units_required
        stock.save()
        req.fulfilled = True
        req.save()
        messages.success(request, "Request fulfilled successfully.")
    else:
        messages.error(request, "Not enough stock to fulfill the request.")
    return redirect('requests_list')


# ------------------- User Authentication -------------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'bloodbank/login.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'bloodbank/register.html')


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')
