from django.urls import path, include
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_profile', views.create_profile, name='create_profile'),
    path('note', views.note, name='note'),
    path('delete_note/<int:id>', views.delete_note, name='delete_note')
]