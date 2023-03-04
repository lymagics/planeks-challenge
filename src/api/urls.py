from django.urls import path, include

urlpatterns = [
    path('schemas/', include('schemas.api.urls')),
]
