from django.urls import path  # type: ignore
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path("new/", BlogCreateView.as_view(), name="blog_new"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("<int:pk>/edit", BlogUpdateView.as_view(), name="blog_edit"),
    path("<int:pk>/delete", BlogDeleteView.as_view(), name="blog_delete"),
    path("", BlogListView.as_view(), name="blogs"),
]
