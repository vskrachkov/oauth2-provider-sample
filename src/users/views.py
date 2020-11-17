from typing import cast

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from oauth2_provider.models import AbstractAccessToken
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class CurrentUserAPIView(RetrieveAPIView):
    permission_classes = [TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self) -> User:
        token = self.request.auth
        if hasattr(token, "scope"):  # OAuth 2
            token = cast(AbstractAccessToken, token)
            if user := token.user:
                self.check_object_permissions(self.request, user)
                return user
        raise NotFound()
