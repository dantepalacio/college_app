from django import forms
from django.forms import Textarea, ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Student, Group

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta(UserCreationForm.Meta):
        model = Student
        fields = UserCreationForm.Meta.fields + ('group',)


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = Student
