from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistrationForm, ProfileForm, PostForm
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


# Create your views here.

# auth views
class MyLoginView(LoginView):
    template_name = 'login.html'

class MyLogoutView(LogoutView):
    template_name = 'logout.html'

class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('success_page')

@login_required
def profile_view(request):
    """
    A view that allows an authenticated user to view and edit their profile details.
    This view handles both GET and POST requests.
    """
    # Get the user's profile object
    profile = request.user.profile

    # This is where we explicitly check the request method
    # It will be 'POST' if the form was submitted
    if request.method == 'POST':
        # If it's a POST request, we pass the data from the form
        form = ProfileForm(request.POST, instance=profile)

        # Check if the form is valid
        if form.is_valid():
            # Save the updated profile data
            form.save()
            
            # Manually update the user's email from the form data
            request.user.email = form.cleaned_data['email']
            request.user.save()

            # Redirect to a success page
            return redirect(reverse('profile_success_page'))
    else:
        # If it's a GET request, we create a form pre-populated with the
        # user's existing profile data.
        form = ProfileForm(instance=profile)

    # Render the template with the form
    return render(request, 'profile.html', {'form': form})


    
class PostListView(ListView):
    model = Post
    template_name = 'listing.html'
    context_object_name = 'posts'
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_blog.html'
    fields = PostForm
    success_url = reverse_lazy('posts') # redirect to all blogs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = date.today
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = PostForm
    success_url = reverse_lazy('posts')

    def test_func(self):
        # This mixin method is used by UserPassesTestMixin.
        # It checks if the logged-in user is the author of the post.
        post = self.get_object()
        return self.request.user == post.author

    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts')

    def test_func(self  ):
        post = self.get_object()
        return self.request.user == post.author
