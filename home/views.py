from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from . import models
from django.views.generic import ListView
from .forms import *


class home_index(ListView):
    model = models.Medicine
    template_name = 'home/index.html'
    context_object_name = "medicines"
    ordering = ["id"]
    paginate_by = 2
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
    
#WORKING ON IT
def search(request):
    template = loader.get_template("home\\index.html")
    context = {}
    if request.method == 'GET':
        form = {"form" : MemberSearchForm(request.GET)}
        context.update(form)
        if form["form"].is_valid():
            query = form["form"].cleaned_data.get('query')
            
            # Perform search on User model
            results = {'results' : models.Medicine.objects.filter(FirstName__icontains=query)}
            context.update(results)
            
            return HttpResponse(template.render(context, request))
    else:
        form = {"form" : MemberSearchForm()}
        context.update(form)
        
    patients = {"medicines" : models.Medicine.objects.all()}
    context.update(patients)
    
    return HttpResponse(template.render(context, request))