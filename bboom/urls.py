from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_post/', views.add_post, name='add_post'),
    path('post_list/', views.post_list, name='post_list'),
    path('', views.user_list, name='user_list'),
    path('register/', views.register, name='register'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('api/users/', views.UserListView.as_view(), name='user_list_api'),
    path('api/users/<int:user_id>/posts/', views.UserPostsView.as_view(), name='user_posts_api'),
    path('api/posts/', views.CreatePostView.as_view(), name='create_post_api'),
    path('api/posts/<int:pk>/', views.DeletePostView.as_view(), name='delete_post_api'),
]
