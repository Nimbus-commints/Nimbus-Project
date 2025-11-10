from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)  # added for the from
from django.urls import reverse_lazy  # added


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "blogs.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blogs")
