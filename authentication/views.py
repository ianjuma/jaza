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

from django.contrib.auth.hashers import make_password


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
        """
        get list of all users
        :param request:
        :param args:
        :param kwargs:
        :return: list of users signed up
        """
        queryset = self.queryset.filter(pk=request.user.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        update a specific user
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.DATA
        first_name = data.pop('firstName', None)
        last_name = data.pop('lastName', None)
        email = data.pop('email', None)
        password = data.pop('password', None)
        update_data = {}

        if first_name is not None:
            update_data['first_name'] = first_name

        if last_name is not None:
            update_data['last_name'] = last_name

        if email is not None:
            update_data['email'] = email

        if password is not None:
            encrypted_password = make_password(password)
            update_data['password'] = encrypted_password

        user = User.objects.get(pk=request.user.id)
        user_serializer = UserSerializer(instance=user, partial=True,
                                         data=update_data)

        if user_serializer.is_valid():
            user_serializer.save()

        return Response(user_serializer.data)

# TODO: static method
