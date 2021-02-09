from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all_games_page, name='games'),
    path('game/<int:pk>', views.GameDetailView.as_view(), name='game'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('my_must/', views.show_must_games_page, name = 'must_games'),
    path('add_to_must/<int:pk>', views.AddToMustView.as_view(), name = 'add_to_must')
]
