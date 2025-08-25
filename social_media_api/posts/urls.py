from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, feed,like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', feed, name='feed'),
    path('', include(router.urls)),
    path("<int:pk>/like/", like_post, name="like_post"),
    path("<int:pk>/unlike/", unlike_post, name="unlike_post"),
]
