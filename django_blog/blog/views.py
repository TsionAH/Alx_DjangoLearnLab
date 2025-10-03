from django.shortcuts import render, get_object_or_404, redirect
from .forms import user_form , ProfileForm , PostForm
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Profile, Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from datetime import date

def blog_home(request):
    return render(request, "home.html")
class MyLoginView(LoginView):
    template_name = 'login.html'
class MyLogoutView(LogoutView):
    template_name = 'logout.html'
class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = user_form
    success_url = reverse_lazy('login')
@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance= profile)
        if form.is_valid():
            form.save()
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect(reverse('posts'))
    else:
        form = ProfileForm(instance = profile)
    return render(request , 'profile.html' , {'form':form})
class PostListView(ListView):
    model = Post
    template_name = 'listing.html'
    context_object_name = 'posts'
class PostDetailView(DetailView):
    model = Post
    template_name = 'create_blog.html'
    fields = PostForm
    success_url = reverse_lazy('posts')
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = date.today
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = PostForm
    success_url = reverse_lazy('posts')

    def test_func(self):
        # This mixin method is used by UserPassesTestMixin.
        # It checks if the logged-in user is the author of the post.
        post = self.get_object()
        return self.request.user == post.author
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_blog.html'
    fields = PostForm
    success_url = reverse_lazy('posts') # redirect to all blogs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = date.today
        return super().form_valid(form)
    
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts')

    def test_func(self  ):
        post = self.get_object()
        return self.request.user == post.author

