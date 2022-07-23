from django.contrib import admin
from authy.models import Profile, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Profile)