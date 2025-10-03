from django.urls import path
from .views import  RegistrationView, LoginView, LogoutView, profile_view, PostListView, PostCreateView , PostDetailView, PostUpdateView, PostDeleteView
from . import views
urlpatterns = [
     path("", views.blog_home, name="home"),  # <-- new
    path("register/", views.RegistrationView.as_view(), name="register"),
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("posts/", views.PostListView.as_view(), name="posts"),
    path("post/new/", views.PostCreateView.as_view(), name="create_post"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-details"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="edit-post"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete-post"),

    # path("", views.blog_home, name="blog-home"),
    # path('register/', RegistrationView.as_view(), name='register'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('profile/', profile_view, name='profile'),

    # path('posts/', PostListView.as_view(template_name='listing.html'), name='posts'),
    # path('post/new/', PostCreateView.as_view(template_name='create_posts.html'), name='create_post'),
    # path('post/<int:pk>/', PostDetailView.as_view(template_name='post_detail.html'), name='post-details'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(template_name='edit_post.html'), name='edit-post'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post')

]