from django.urls import path  # type: ignore
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("", BlogListView.as_view(), name="blogs"),
]
