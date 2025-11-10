from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "blogs.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"
