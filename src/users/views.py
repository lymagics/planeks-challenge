from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginPageView(LoginView):
    """
    View for displaying the login page.
    """
    pass


class LogoutPageView(LoginRequiredMixin, LogoutView):
    """
    View for logging out the user and redirecting to the home page.
    """
    pass
