from re import template
from tokenize import Name
from unicodedata import name
from django.urls import path, include
from authy.views import UserProfile, EditProfile
from django_registration.backends.activation.views import RegistrationView
from .forms import AuthyRegistrationForm
from django.contrib.auth import views as auth_views #changed from authViews to auth_views



urlpatterns = [
   	
    path('profile/edit', EditProfile, name='edit-profile'),
	path('accounts/profile/', UserProfile, name='profile'),
	path('accounts/', include('django.contrib.auth.urls')),
	path("accounts/register/", RegistrationView.as_view(form_class=AuthyRegistrationForm), name="django_registration_register"),
	path("accounts/", include("django_registration.backends.activation.urls"))


# ## Password reset as seen in django documentation
	
# 	# #submit email form
# 	path('reset_password/', auth_views.PasswordResetView.as_view( template_name="authy/password_reset.html"),
# 	name="reset_password"),
	
# 	## email sent success message
# 	path('reset_password_done/', auth_views.PasswordResetDoneView.as_view( template_name="authy/password_reset_done.html"), 
# 	name="password_reset_done"),
	
# 	##link to password reset sent to  email
# 	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() name="password_reset_confirm"),
	
# 	##password successfully changed completed
# 	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="authy/password_reset_complete.html"),
# 	name="password_reset_complete"),

]