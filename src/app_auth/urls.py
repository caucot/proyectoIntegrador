from django.urls import path 
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'app_auth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]