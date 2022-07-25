from django.urls import path, include
from authy.views import UserProfile, Signup, EditProfile

from django.contrib.auth import views as authViews 



urlpatterns = [
   	
    path('profile/edit', EditProfile, name='edit-profile'),
	path('accounts/profile/', UserProfile, name='profile'),
   	path('accounts/signup/', Signup, name='signup'),
	path('accounts/', include('django.contrib.auth.urls')),


]