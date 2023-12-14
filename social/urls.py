from django.contrib import admin
from django.urls import path

from .views import HomeView, EquipmentView, GamesView, ForumView, HeadsetsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('equipment', EquipmentView.as_view(), name="equipment"),
    path('games', GamesView.as_view(), name="games"),
    path('forum', ForumView.as_view(), name="forum"),
    path('headsets', HeadsetsView.as_view(), name="headsets"),
]
