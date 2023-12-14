from django.shortcuts import render
from django.views import View


# class HomeView(View):
#     def get(self, request):
#         context = {}  # Add your context data here
#         return render(request, 'home.html', context)
    

# class EquipmentView(View):
#     def get(self, request):
#         context = {}  # Add your context data here
#         return render(request, 'equipment.html', context)


class MyView(View):
    def get(self, request):
        context = {}  # Add your context data here
        return render(request, self.template_name, context)


class HomeView(MyView):
    template_name = 'home.html'


class EquipmentView(MyView):
    template_name = 'equipment.html'


class GamesView(MyView):
    template_name = 'games.html'
