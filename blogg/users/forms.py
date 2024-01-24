from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Rec
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Rec
        fields = ('username', 'email', 'age',)
class ChangeForm(UserChangeForm):
    class Meta:
        model = Rec
        fields = ('username', 'email', 'age',)