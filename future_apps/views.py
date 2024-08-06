import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Brand, User, Profile
from .forms import PostForm, EditForm, ProfilePageForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Pagination here
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.views import generic


# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        messages.error(request, 'You need to create a profile first.')
        return redirect('create_profile')

    if request.method == 'POST':
        form = ProfilePageForm(request.POST, request.FILES, instance=profile, user_is_premium=request.user.profile.is_premium)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile', user_id=request.user.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfilePageForm(instance=profile, user_is_premium=request.user.profile.is_premium)

    return render(request, 'registration/edit_profile_page.html', {'form': form})


def profile_view(request):
    return render(request, 'registration/profile.html', {'user': request.user})


# Stripe codes
stripe.api_key = settings.STRIPE_SECRET_KEY

def upgrade_to_premium(request):
    # Check if the user has a profile
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # If the user doesn't have a profile, display an error message
        messages.error(request, 'Create a profile before upgrading to premium.')
        return redirect('edit_profile')
    
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=1000,  # amount in cents
                currency='usd',
                description='Premium Subscription',
                source=token,
            )
            profile.is_premium = True
            profile.save()
            return redirect('profile')
        except stripe.error.StripeError:
            return render(request, 'payment/error.html', {'error': 'An error occurred during payment processing.'})

    return render(request, 'payment/upgrade.html', {'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})



def search_shoes(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        posts = Post.objects.filter(
            Q(brand__name__icontains=searched) |  # Correct lookup for the ForeignKey field
            Q(model__icontains=searched) |
            Q(colaboration__icontains=searched) |
            Q(color_scheme_1__icontains=searched) |
            Q(color_scheme_2__icontains=searched) |
            Q(color_scheme_3__icontains=searched) |
            Q(author__username__icontains=searched)
        )
        users = User.objects.filter(username__icontains=searched)

        # Pagination set up
        p = Paginator(posts.order_by('brand__name'), 5)  # Order by brand name
        page = request.GET.get('page')
        posts_list = p.get_page(page)

        return render(request, 'search_shoes.html', {
            'searched': searched.title(),
            'posts': posts,
            'posts_list': posts_list,
            'users': users,
        })
    else:
        return render(request, 'search_shoes.html', {})


def index(request):
    return render(request, 'hangman.html')

def shoen_meta(request):
    return render(request, 'shoen_meta.html')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    
    
def BrandView(request, brand):
    brand_posts = Post.objects.filter(brand=brand)    
    return render(request, 'brand.html', {'brand':brand, 'brand_posts':brand_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        nod = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = nod.total_likes()
        
        liked = False
        if nod.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
    def form_valid(self, form):
        user = self.request.user
        post_count = Post.objects.filter(author=user).count()

        if not user.profile.is_premium and post_count >= 5:
            messages.error(self.request, 'Free users can only add 5 Virtual Closet entries. Please upgrade to premium for Unlimited!')
            return redirect('home')

        form.instance.author = user
        return super().form_valid(form)
    
class AddBrandView(CreateView):
    model = Brand
    template_name = 'add_brand.html'
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'body']
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
