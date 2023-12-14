from django.urls import path

from .views import HomeView, EquipmentView, GamesView, ForumView, HeadsetsView, UserRegistrationView, UserLoginView, UserLogoutView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('equipment', EquipmentView.as_view(), name="equipment"),
    path('games', GamesView.as_view(), name="games"),
    path('forum', ForumView.as_view(), name="forum"),
    path('headsets', HeadsetsView.as_view(), name="headsets"),

    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]
