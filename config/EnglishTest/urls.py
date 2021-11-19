from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.RegisrerView.as_view(), name='register'),
    path('start_test/', views.TestingType.as_view(), name='start_tests'),
    path('cabinet/', views.CabinetView.as_view(), name='cabinet'),
]
