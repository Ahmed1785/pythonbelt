from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
import re 
import bcrypt
from datetime import datetime


class TravelManager(models.Manager):
    def validate_review(self, post_data):
        results = {"errors": [], "status": False}
        if len(post_data['destination']) < 1:
            results["errors"].append("please enter a destination")
            results["status"] = True

        if len(post_data['description']) < 1:
            results["errors"].append("please enter a description")
            results["status"] = True

        if len(post_data['description']) < 1:
            results["errors"].append("please enter a description")
            results["status"] = True


        return results


class Travel(models.Model):
    destination = models.TextField(max_length=100)
    description = models.TextField(max_length=150)
    travel_date = models.DateField()
    arrive_date = models.DateField()
    travelplanner_id = models.ForeignKey(User, related_name="travelplanner")
    travelmaker_id = models.ManyToManyField(User, related_name="travelmaker")
    travelManager = TravelManager()
    objects = models.Manager()
