from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, ProfileView, PostListCreateView, PostDetailView, AddCommentView, CustomLoginView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout URL
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('posts/', PostListCreateView.as_view(), name='post_list_create'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('add_comment/<int:post_id>/', AddCommentView.as_view(), name='add_comment'),
    
]
