from django.shortcuts import render
from .models import UserProfileModel
from django.views.generic import FormView, DetailView
# Create your views here.

#User model view
class UserView(DetailView):
    model = UserProfileModel