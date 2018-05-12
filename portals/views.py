from django.shortcuts import render
from django.views.generic import FormView, CreateView
from portals.forms import CreateForm
from django.urls import resolve, reverse_lazy
from django.contrib import messages

def home(request):
    return render(request, 'portals/HomePage.html')


class CreateItem(CreateView):
    form_class = CreateForm
    template_name = 'portals/navbar.html'
    success_url = reverse_lazy('home_page')





