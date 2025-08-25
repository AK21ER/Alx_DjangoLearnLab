from django.urls import path, include

urlpatterns = [
    path("posts/", include("posts.urls")),
    path("notifications/", include("notifications.urls")),
]
