from django.contrib import admin
from django.urls import path

from .views import HomeView, EquipmentView, GamesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('equipment', EquipmentView.as_view(), name="equipment"),
    path('games', GamesView.as_view(), name="games"),
]
