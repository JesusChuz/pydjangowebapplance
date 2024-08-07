from django import forms 
from .models import Post, Brand, Profile
from future_apps.models import Profile


shoes = Brand.objects.all().values_list('name', 'name')

shoe_list = []

for item in shoes:
    shoe_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'brand', 'model', 'colaboration', 'color_scheme_1', 'color_scheme_2', 'color_scheme_3', 'body', 'shoe_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'phil', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            # 'brand': forms.Select(choices=shoe_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'shoe_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'linkedin_url', 'instagram_url', 'twitter_url', 'meta_url', 'pinterest_url', 'soundcloud_url', 'youtube_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
            'soundcloud_url': forms.TextInput(attrs={'class': 'form-control'}),
            'youtube_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'bio', 'profile_pic', 'linkedin_url', 'instagram_url', 'twitter_url', 'meta_url', 
            'pinterest_url', 'soundcloud_url', 'youtube_url'
        )
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control'}),
            'meta_url': forms.URLInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.URLInput(attrs={'class': 'form-control'}),
            'soundcloud_url': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user_is_premium = kwargs.pop('user_is_premium', False)
        super(ProfilePageForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        social_links = [
            cleaned_data.get('linkedin_url'),
            cleaned_data.get('instagram_url'),
            cleaned_data.get('twitter_url'),
            cleaned_data.get('meta_url'),
            cleaned_data.get('pinterest_url'),
            cleaned_data.get('soundcloud_url'),
            cleaned_data.get('youtube_url')
        ]
        
        # Count the number of non-empty social links
        non_empty_links = sum(1 for link in social_links if link)
        
        # Check if user is premium
        if not self.user_is_premium and non_empty_links > 1:
            raise forms.ValidationError("Free users can only provide one social media link.")

        return cleaned_data

