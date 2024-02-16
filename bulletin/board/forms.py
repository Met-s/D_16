from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "post_author",
            "post_title",
            "post_category",
            "post_text",
        ]


class CustomSignUpForm(SignupForm):
    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        author = Group.objects.get(name='Author')
        author.user_set.add(user)
        return user
