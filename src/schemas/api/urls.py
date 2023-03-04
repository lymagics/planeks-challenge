from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.generate_csv_data, name='generate-schema'),
]
