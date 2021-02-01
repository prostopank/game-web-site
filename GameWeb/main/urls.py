from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.GameListView.as_view(), name='games'),
    path('accounts/', include('django.contrib.auth.urls')),
]
