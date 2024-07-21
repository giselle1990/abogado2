from django.urls import path
from . import views
from .views import user_logout

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
