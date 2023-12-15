from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, UserLoginSerializer


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


class HeadsetsView(MyView):
    template_name = 'headsets.html'


class ForumView(MyView):
    template_name = 'forum.html'


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')  # Redirect to the home page if 'next' is not present
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class UserLogoutView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         logout(request)
#         return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
