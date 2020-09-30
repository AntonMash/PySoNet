from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer


# class GetUserNetView(RetrieveAPIView):
#     """Вывод профиля пользователя"""
#     queryset = UserNet.objects.all()
#     serializer_class = GetUserNetSerializer


# class UpdateUserNet(UpdateAPIView):
#     """Редактироание пользователя"""
#
#     serializer_class = GetUserNetSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return UserNet.objects.filter(id=self.request.user.id)

class UserNetPublicView(ModelViewSet):
    """Вывод публичного профиля пользователя"""
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetView(ModelViewSet):
    """Вывод профиля пользователя"""
    # queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
