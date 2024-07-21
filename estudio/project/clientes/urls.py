from django.urls import path
from .views import clientes_list, expedientes, index
from accounts.views import user_login, register, user_logout

urlpatterns = [
    path('', index, name='index'),
    path('clientes/', clientes_list, name='clientes_list'),
    path('expedientes/', expedientes, name='expedientes'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
]
