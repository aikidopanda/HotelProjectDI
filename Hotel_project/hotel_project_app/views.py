from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from utils import *
from django.views.generic import (
                                # CreateView,
                                # UpdateView
                                )
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from forms import (
                ReserveForm,
                LookApartmentForm
                )
from .models import (
                    # Booking,
                    # Room
                    )
from datetime import datetime
from django.contrib import messages

# Create your views here.

class UserAuthentication(LoginView):
    form_class = AuthenticationForm
    template_name ='login.html'
    success_url = reverse_lazy('homepage')

def logout_user (request):
    logout(request)
    return redirect('homepage')