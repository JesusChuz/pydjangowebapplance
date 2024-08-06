from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, EditProfileForm, PasswordChangeForm, ProfilePageForm
from django.contrib.auth.models import User
from future_apps.models import Profile, Post 
from django.contrib import messages
# Import Pagination Here
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView




# Create your views here.


def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        messages.error(request, 'You need to create a profile first.')
        return redirect('create_profile')

    if request.method == 'POST':
        form = ProfilePageForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile', user_id=request.user.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfilePageForm(instance=profile, user=request.user)

    return render(request, 'registration/edit_profile_page.html', {'form': form})


def my_collection(request):
    if request.user.is_authenticated:
        me = request.user.id
        
        # Ensure we are ordering by the brand name
        posts = Post.objects.filter(author=me).order_by('brand__name')
        shoe_count = Post.objects.filter(author=me).count()

        # Collection counter
        if shoe_count == 3:
            messages.success(request, 'NICE COLLECTION!')
            print(f'{shoe_count}: NICE COLLECTION!')

        elif shoe_count == 25:
            messages.success(request, 'COOL COLLECTION!')
            print(f'{shoe_count}: COOL COLLECTION!')

        elif shoe_count == 100:
            messages.success(request, 'DOPE COLLECTION!')
            print(f'{shoe_count}: DOPE COLLECTION!')

        elif shoe_count == 500:
            messages.success(request, 'SUPREME CLIENTELE!')
            print(f'{shoe_count}: SUPREME CLIENTELE!')

        elif shoe_count == 755:
            messages.success(request, 'SHOELLIONAIRE STATUS!')
            print(f'{shoe_count}: SHOELLIONAIRE STATUS!')

        # Pagination setup
        p = Paginator(posts, 25)
        page = request.GET.get('page')
        posts_list = p.get_page(page)
        nums = "a" * posts_list.paginator.num_pages

        return render(request, 'registration/my_collection.html', {
            'posts': posts,
            'posts_list': posts_list,
            'shoe_count': shoe_count,
            'nums': nums,
        })

    else:
        # You cannot view My Collection from Article details.html unless logged in.
        return redirect('home')


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    success_url = reverse_lazy('home')  # or another appropriate URL

    # These arguments are the single user restrictions and message Free users can use only 1 link
    def get_form_kwargs(self):
        kwargs = super(CreateProfilePageView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        profile, created = Profile.objects.get_or_create(user=user)
        form.instance.user = user
        form.instance.id = profile.id  # Set the ID to update the existing profile
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error(None, "An error occurred while creating the profile.")
            return self.form_invalid(form)
                    
class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    # fields = ['bio', 'profile_pic', 'linkedin_url', 'instagram_url', 'twitter_url', 'meta_url', 'pinterest_url', 'soundcloud_url', 'youtube_url'] 
    success_url = reverse_lazy('home')
    
    def get_form_kwargs(self):
        kwargs = super(EditProfilePageView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error(None, "An error occurred while updating the profile.")
            return self.form_invalid(form)


class ShowProfilePageView(DetailView):
    model = Post
    template_name = 'registration/user_profile.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        page_user = Post.objects.filter(id=self.kwargs['pk'])
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        # page_user = get_object_or_404(Post, id=self.kwargs['pk'])

        context['page_user'] = page_user        
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('login')
    
    def get_object(self):
        return self.request.user
    
    
    
    