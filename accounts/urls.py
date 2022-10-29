from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, UserAccountView, UpdateUserAccountView




urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", logout_view, name='logout'),
    path("register/", RegisterView.as_view(), name='register'),
    path("user/<int:pk>", UserAccountView.as_view(), name='user_page'),
    path("user/<int:pk>/update_info", UpdateUserAccountView.as_view(), name='update_user_page'),
]