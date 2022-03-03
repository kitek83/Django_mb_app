from django.shortcuts import render
from .models import Post
from django.views.generic import ListView  #returns object_list
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'  #dafault name object_list

