from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomeView, EquipmentView, GamesView, ForumView, HeadsetsView, UserRegistrationView, UserLoginView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('equipment', EquipmentView.as_view(), name="equipment"),
    path('games', GamesView.as_view(), name="games"),
    path('forum', ForumView.as_view(), name="forum"),
    path('headsets', HeadsetsView.as_view(), name="headsets"),

    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    # path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='user_logout'),
]
