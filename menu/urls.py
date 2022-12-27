from django.urls import path

from .views import MainMenuView


urlpatterns = [
        path('', MainMenuView.as_view(), name='main_menu'),
    ]
