from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm
class Mailgb(TemplateView):
    template_name = "mail.html"

class CreateUser(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("index")
    template_name= 'reg.html'

class PopListView(ListView):
    model = User
    context_object_name = "Popo"
    template_name = 'reg.html'

class UserList(ListView):
      model = User
      context_object_name = "users"
      template_name = 'index.html'