from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm , CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])  # Use 'password1'
        user.save()
        login(self.request, user)  # Log in the user after registration
        return redirect(self.success_url)  # Use self.success_url directly


class CustomLoginView(LoginView):
    template_name = 'social/login.html'
    success_url = reverse_lazy('profile')

    
class ProfileView(LoginRequiredMixin, TemplateView):  # Converted to a class-based view
    template_name = 'social/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Add the user to the context
        return context

class PostListCreateView(LoginRequiredMixin, View):
    template_name = 'social/post_list_create.html'  # Correct template path
    
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')  # Get all posts ordered by created_at
        form = PostForm()  # Initialize the post form
        return render(request, self.template_name, {'posts': posts, 'form': form})
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Associate the post with the logged-in user
            post.save()
            return redirect('post_list_create')  # Redirect back to the post list
        posts = Post.objects.all().order_by('-created_at')  # Fetch posts again for rendering the form errors
        return render(request, self.template_name, {'posts': posts, 'form': form})
    
class PostDetailView(LoginRequiredMixin, View):
    template_name = 'social/post_detail.html'  # Template for displaying a single post

    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)  # Get the specific post
        comments = post.comments.all().order_by('-created_at')  # Reverse order of comments
        form = CommentForm()  # Initialize the comment form
        return render(request, self.template_name, {
            'post': post,
            'comments': comments,
            'form': form
        })

    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)  # Get the specific post
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Link comment to the post
            comment.user = request.user  # Link comment to the logged-in user
            comment.save()
            return redirect('post_detail', post_id=post.id)  # Redirect to the post detail view
        comments = post.comments.all().order_by('-created_at')  # Fetch comments again for rendering the form errors
        return render(request, self.template_name, {
            'post': post,
            'comments': comments,
            'form': form
        })
    

class AddCommentView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'social/add_comment.html'  # Correct template path
    
    def form_valid(self, form):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        form.instance.post = post  # Link comment to the post
        form.instance.user = self.request.user  # Link comment to the logged-in user
        form.save()
        return redirect('post_list_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs['post_id']
        context['post'] = get_object_or_404(Post, id=post_id)
        return context

