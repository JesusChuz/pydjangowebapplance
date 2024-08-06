from django.urls import path
from .views import upgrade_to_premium
from django.contrib.auth.views import LogoutView
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddBrandView, BrandView, LikeView, profile_view
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_brand/', AddBrandView.as_view(), name='add_brand'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('brand/<str:brand>/', BrandView, name='brand'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('hangman', views.index, name='hangman'),
    path('shoen_meta', views.shoen_meta, name='shoen_meta'),
    path('search_shoes', views.search_shoes, name='search_shoes'),  
    path('upgrade_to_premium/', upgrade_to_premium, name='upgrade_to_premium'), 
    path('profile/', profile_view, name='profile'), 

]
