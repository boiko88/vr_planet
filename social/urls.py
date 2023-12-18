from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomeView, EquipmentView, GamesView, ForumView, HeadsetsView, UserRegistrationView, BlogView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('equipment', EquipmentView.as_view(), name="equipment"),
    path('games', GamesView.as_view(), name="games"),
    path('forum', ForumView.as_view(), name="forum"),
    path('headsets', HeadsetsView.as_view(), name="headsets"),
    path('blog', BlogView.as_view(), name="blog"),
    path('login/', auth_views.LoginView.as_view(template_name='login1.html', success_url='/'), name='login'),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    # path('user_login/', LoginView.as_view(), name='user_login'),
    # path('login1/', LoginView.as_view(), name='login1'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='user_logout'),
]
