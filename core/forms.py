from .models import Profile
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta: 
        model = Profile
        fields = {'location', 'birth_date', 'bio'}