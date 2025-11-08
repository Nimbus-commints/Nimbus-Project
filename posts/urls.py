from django.urls import path  # type: ignore
from .views import PostPageViews

urlpatterns = [
    path("", PostPageViews.as_view(), name="posts"),
]
