from django.urls import path, include
from authy.views import UserProfile, EditProfile
from django_registration.backends.activation.views import RegistrationView
from .forms import AuthyRegistrationForm
from django.contrib.auth import views as authViews 



urlpatterns = [
   	
    path('profile/edit', EditProfile, name='edit-profile'),
	path('accounts/profile/', UserProfile, name='profile'),
	path('accounts/', include('django.contrib.auth.urls')),
	path("accounts/register/", RegistrationView.as_view(form_class=AuthyRegistrationForm), name="django_registration_register"),
	path("accounts/", include("django_registration.backends.activation.urls"))


]