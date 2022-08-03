from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import register, Profile
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html", success_url=reverse_lazy('password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"), name='password_change_done'),
    path('profile/', login_required(Profile.as_view()), name='profile'),
]
