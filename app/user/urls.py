from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user import views

app_name = 'user'

urlpatterns = [
    path('register/',views.CreateUserView.as_view(), name = 'register'),
    path('login/',views.LoginUserView.as_view(), name = 'login'),
    path('logout/',views.LogoutUserView.as_view(), name = 'logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
