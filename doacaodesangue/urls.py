from django.urls import path
from .views import list_donor, create_donor, update_donor, delete_donor
from .views import list_doctor, create_doctor, update_doctor, delete_doctor

urlpatterns = [
    path('', list_donor, name='list_donor'),
    path('new', create_donor, name='create_donor'),
    path('update/<int:id>/', update_donor, name='update_donor'),
    path('delete/<int:id>/', delete_donor, name='delete_donor'),
]