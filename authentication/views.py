import json
from django.contrib.auth import login, logout, authenticate
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth.models import User
from authentication.permissions import IsAccountOwner
from authentication.serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination


@permission_classes((AllowAny,))
class Login(views.APIView):

    def post(self, request, format=None):
        data = json.loads(request.body)

        username = str(data.get('username'))
        password = str(data.get('password'))

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                serialized = UserSerializer(user)
                return Response(serialized.data)
            else:
                return Response({'status': 'Unauthorised',
                                 'message': 'This account has been disabled'},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'status': 'Unauthorised',
                             'message': 'Wrong Username or Password'},
                            status=status.HTTP_401_UNAUTHORIZED)


@permission_classes((AllowAny,))
class Logout(views.APIView):

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        return permissions.IsAuthenticated(), IsAccountOwner()

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(pk=request.user.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

# TODO: static method
