from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Lesson, Post
from tinymce.widgets import TinyMCE

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class AddLessonForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE())
    class Meta:
        model = Lesson
        fields = ('title', 'description', 'video_url')

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'image')