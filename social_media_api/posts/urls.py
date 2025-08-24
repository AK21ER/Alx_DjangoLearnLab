from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet ,
from .views import feed
from django.urls import path
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = router.urls + [
    path('feed/', feed, name='feed')
]

