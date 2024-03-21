from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from . import models
from home.models import *
from .forms import *
from django.contrib import messages
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from time import sleep


def Register(request):
    if request.method == "POST":
        form = UserReg(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"account created for {user} successfuly")
            return redirect("home_index")
        else:
            messages.error(request, "account not created")
    else:
        form = UserReg()
            
    template = loader.get_template("users/register.html")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


class profile(LoginRequiredMixin, ListView):
    model = Medicine
    template_name = 'users/profile.html'
    context_object_name = "meds"
    paginate_by = 6
    
    def get_queryset(self):
        # Filter the queryset based on the current user
        return super().get_queryset().filter(author=self.request.user)
        
    
    

class AddMedication(LoginRequiredMixin, CreateView):
    model = Medicine
    fields = [
        "Disease", "Medication", "Dose", "start", "end"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    


class SpecificMedication(LoginRequiredMixin, DetailView):
    model = Medicine

class DeleteMedication(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Medicine
    success_url = '/'
    
    def test_func(self):
        medication = self.get_object()
        if self.request.user != medication.author:
            return True
        return False
