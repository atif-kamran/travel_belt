from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Trip, Join
from datetime import datetime, date
from django import forms

def index(request):
    if 'name' in request.session:
        return redirect('/travels')
    return render(request, "regsnlogs/index.html")

def register(request):
    if request.method == "POST":
        result = User.objects.register(request)
        if result[0] == False:
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            messages.success(request, 'Registration successful')
    return redirect("/")

def login(request):
    if request.method == "POST":
        result = User.objects.login(request)
        if result[0] == False:
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            request.session['name']= result[1].name
            request.session['id'] = result[1].id
            return redirect('/travels')
    return redirect("/")

def travels(request):
    if 'name' in request.session:
        trips = Trip.objects.exclude(join__user_id=request.session['id'])
        joins = Join.objects.filter(user_id=request.session['id'])
        context = {
            "trips": trips,
            "joins": joins
        }
        return render(request, "regsnlogs/success.html", context)
    return redirect('/')

def add_plan(request):
    if 'name' in request.session:

        return render(request, 'regsnlogs/specific.html')
    return redirect('/')

def plan_time(request, id):
    if 'name' in request.session:
        destination = request.POST['destination']
        description = request.POST['description']
        departing = request.POST['departing']
        returning = request.POST['returning']

        if len(destination) < 1 or len(description) < 1:
            if len(destination) < 1:
                messages.warning(request, 'Destination cannot be left blank')
            if len(description) <1:
                messages.warning(request, 'Description cannot be left blank')
            if departing <= datetime.date.today():
                messages.warning("The date cannot be today or in the past!")
            if departing <= datetime.date.today():
                messages.warning("The date cannot be today or in the past!")
        else:
            user = User.objects.get(id=id)
            add_trip = Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], departing=request.POST['departing'], returning=request.POST['returning'], user=user)
        return redirect('/travels')
    return redirect('/')

def join_plan(request, id, tid):
    user = User.objects.get(id=id)
    trip = Trip.objects.get(id=tid)
    join_trip = Join.objects.create(user=user, trip=trip)
    return redirect('/travels')

def destination(request, id):
    user = User.objects.get(id=id)
    trips = Trip.objects.filter(user_id=id)
    join = Join.objects.filter(user_id=id)
    context = {
        'user': user,
        'trips': trips,
        'joins':joins
    }
    return render(request, 'regsnlogs/destination.html', context)

def logout(request):
    if 'name' in request.session:

        request.session.clear()
    return redirect('/')
