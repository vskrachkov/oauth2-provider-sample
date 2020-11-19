from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class CurrentUserAPIView(RetrieveAPIView):
    queryset = User.objects.none()
    serializer_class = UserSerializer

    def get_object(self) -> User:
        if user := self.request.user:
            return user
        raise NotFound()
