from django.urls import path
from .views import RegistrationView, LoginView, ProfileView, PasswordChangeview

app_name = 'account'
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('password-change/', PasswordChangeview.as_view(), name="password-change")
]
