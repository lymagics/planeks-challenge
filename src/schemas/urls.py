from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.SchemaCreateView.as_view(), name='new'),
    path('<int:pk>/', views.SchemaDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.SchemaUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.SchemaDeleteView.as_view(), name='delete'),
    path('', views.SchemaListView.as_view(), name='list'),
    path('dataset/<int:pk>/download/', views.download_dataset, name='download'),
]

app_name = 'schemas'
