from __future__ import unicode_literals
from models import Travel
from ..login_app.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
import datetime


def dashboard(request):
    if "first_name" not in request.session:
        return redirect("/")
    context = {
        "other_users": Travel.objects.exclude(id = request.session["id"]),
        "cur_user": User.objects.get(id = request.session["id"]),
        "travels": Travel.objects.all() 
    }

    return render(request, "second_app/dashboard.html", context)

def addTravel(request):
    return render(request, "second_app/add.html")

def home(request):
    return redirect("/second_app/dashboard")

def create(request):
    # if request.POST["travel_date"] < datetime.date.today():
    #     return redirect ("/second_app/add.html")
    # else:
        user = User.objects.get(id = request.session["id"])
        Travel.objects.create(destination = request.POST["destination"], description = request.POST["description"], travel_date = request.POST["travel_date"], arrive_date = request.POST["arrive_date"], travelplanner_id = user)
        return redirect("/second_app/dashboard")

def join(request, id):
    travel = Travel.objects.get(id=id)
    user = User.objects.get(id = request.session["id"])
    user.travelplanner.add(travel)
    return redirect("/second_app/dashboard")

def unjoin(request, id):
    # user = User.objects.get(id = request.session["id"])
    Travel.objects.get(id=id).delete()
    return redirect("/second_app/dashboard")

def showUser(request, id):
    context = {
        "travel": Travel.objects.get(id=id)
    }
    return render(request, "second_app/show.html", context)