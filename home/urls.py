from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('create/', views.create_record, name='create_record'),  # Создание записи
    path('edit/<int:pk>/', views.edit_record, name='edit_record'),  # Редактирование записи
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),  # Удаление записи
]
