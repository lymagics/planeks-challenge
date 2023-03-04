from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form used in the admin panel.
    """

    class Meta:
        model = User
        fields = ('username', 'password',)


class CustomUserChangeForm(UserChangeForm):
    """
    Custom user change form used in the admin panel.
    """

    class Meta:
        model = User
        fields = ('username',)
