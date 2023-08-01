from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import Post, UserProfile
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, PostSerializer


@login_required
def add_post(request):
    if request.method == 'POST':
        # Process the form submission and save the post
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user  # The current authenticated user

        post = Post.objects.create(title=title, content=content, user=user)
        # Redirect to a page that displays all posts or the post detail page
        return redirect('post_list')
    
    # If it's a GET request, render the form template
    return render(request, 'add_post.html')



@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user == post.user:
        post.delete()

    return redirect('post_list')



def post_list(request):
    # Get all posts from the database
    posts = Post.objects.all()
    
    # Pass the posts to the template for rendering
    return render(request, 'post_list.html', {'posts': posts})


def user_list(request):
    # Get all users from the database
    users = User.objects.all()

    # Pass the users to the template for rendering
    return render(request, 'user_list.html', {'users': users})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})




@login_required
def user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If the user profile does not exist, create one
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    return render(request, 'user_profile.html', {'user_profile': user_profile})




class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(user__id=user_id)

class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class DeletePostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]