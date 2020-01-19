from .models import Profile, Note
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta: 
        model = Profile
        fields = {'location', 'birth_date', 'bio'}

class NoteForm(ModelForm):
    class Meta :
        model = Note 
        field_order =['title','body','image']
        # fields = {'title', 'body', 'image'}
        exclude = {'user', 'pub_date'}