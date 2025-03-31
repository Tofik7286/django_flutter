from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
