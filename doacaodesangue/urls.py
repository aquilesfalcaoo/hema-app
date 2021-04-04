from django.urls import path
from .views import list_doador, create_doador, update_doador, delete_doador
from .core import views

urlpatterns = [
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', list_doador, name='list_doador'),
    path('new', create_doador, name='create_doador'),
    path('update/<int:id>/', update_doador, name='update_doador'),
    path('delete/<int:id>/', delete_doador, name='delete_doador'),
]
