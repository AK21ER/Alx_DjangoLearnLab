# blog/urls.py
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', views.home, name='home'),  # <-- this defines 'home'
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path('posts/', views.posts, name='posts'),  # <- Make sure this exists
    path('', PostListView.as_view(), name='home'),  # list all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # create
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # detail
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # update
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # delete
]

