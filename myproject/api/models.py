from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # ✅ Default User model se connected
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    gender = models.CharField(max_length=1, choices=gender_choices)
    profile_pic = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)  # ✅ Profile Picture
    hobbies = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
