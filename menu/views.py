from django.views import View
from django.shortcuts import render


class MainMenuView(View):

    def get(self, request):

        return render(request, 'menu/main.html')
