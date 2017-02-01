from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from datetime import datetime, date
from django import forms

class UserManager(models.Manager):

    def register(self, request):
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_pw = request.POST['confirm_pw']

        reg_errors = []

        valid = True
        if len(name) < 1 or len(username) < 1 or len(password) < 1 or len(confirm_pw) < 1:
            reg_errors.append("A field cannot be left blank!")
            valid = False

        else:
            # names
            if len(name) < 3 or len(username) < 3:
                errors.append("Name field needs at least two characters")
                valid = False
            elif name.isalpha() == False or username.isalpha() == False:
                errors.append("Name field needs to be all letters")
                valid = False
            # password
            if len(password) < 8:
                errors.append("Password needs at least 8 characters")
                valid = False
            elif password != confirm_pw:
                errors.append("Password and confirm password needs to match")
                valid = False

        if valid:
            unique_list = User.objects.filter(username = username)
            if not unique_list:
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                user = User.objects.create(name=name, username=username, password=pw_hash)
                return (True, user)
            else:
                errors.append("Username already exists")

        return (False, errors)

    def login(self, request):
        if request.method == "POST":
            username = request.POST['username_log'].lower()
            password = request.POST['password_log']

            login_messages = []

            if len(username) < 1 or len(password) < 1:
                login_messages.append("A field can not be empty")

            if len(password) < 8:
                login_messages.append("Passwords needs at least 8 characters")

            if not login_messages:
                user = User.objects.filter(username=username)
                if user:
                    if bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password.encode():
                        return True, user[0]
                    else:
                        login_messages.append("Wrong password")
                else:
                    login_messages.append("Not a registered user")

        return False, login_messages


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    user = models.ForeignKey(User)
    destination = models.CharField(max_length=255)
    departing = models.DateField()
    returning = models.DateField()
    description = models.CharField(max_length=1500)

class Join(models.Model):
    user = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)

# Create your models here.
