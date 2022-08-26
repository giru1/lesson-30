from django.http import JsonResponse
import json

from django.http import JsonResponse
# Create your views here.
from django.views.generic import UpdateView, DeleteView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from users.models import User, Location
from users.serializers import UserDetailSerializer, UserListSerializer, UserCreateSerializer, LocationSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def post(self, request, *args, **kwargs):
        user = UserCreateSerializer(data=json.loads(request.body))

        user.save() if user.is_valid() else JsonResponse(user.errors)

        return JsonResponse(user.data)


class UserUpdateView(UpdateView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
