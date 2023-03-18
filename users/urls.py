from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import \
    LogoutView  # если доделаем логин через логинвью
from django.urls import path

from users.views import EmailVerificationView  # , logout, login
from users.views import UserLoginView, UserProfileView, UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),  # если доделаем логин через логинвью
    # path('login/', login, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),  # если доделаем логин через логинвью
    # если доделаем логин через логинвью
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
    # path('logout/', logout, name='logout'),
]
