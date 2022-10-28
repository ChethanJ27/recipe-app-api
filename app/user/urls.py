from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('register/',views.CreateUserView.as_view(), name = 'register'),
    path('login/',views.LoginUserView.as_view(), name = 'login'),
]
