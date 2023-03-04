from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import User
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Django admin model to represent the user model in the admin panel.
    """

    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('id', 'username',)
    list_display_links = ('username',)
