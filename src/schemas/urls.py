from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.create_schema, name='schema_new'),
    path('<int:pk>/', views.SchemaDetailView.as_view(), name='schema_detail'),
    path('<int:pk>/edit/', views.update_schema, name='schema_update'),
    path('<int:pk>/delete/', views.SchemaDeleteView.as_view(), name='schema_delete'),
    path('', views.SchemaListView.as_view(), name='schema_list'),
    path('dataset/<int:pk>/download/', views.download_dataset, name='dataset_download'),
]
