import json
from django.contrib.auth import login, logout, authenticate
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth.models import User
from authentication.permissions import IsAccountOwner
from authentication.serializers import UserSerializer
from ast import literal_eval


@permission_classes((AllowAny,))
class Login(views.APIView):

    def post(self, request, format=None):
        # print type(request.data)
        # data = json.loads(request.data)
        # data = literal_eval(request.data)
        print data
        password = data.get('password')
        username = data.get('username')
        print type(password)

        # data = literal_eval(data)
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active():
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


@permission_classes((IsAuthenticated, IsAccountOwner))
class Logout(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


@permission_classes((IsAuthenticated,))
class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return permissions.IsAuthenticated(), IsAccountOwner()

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(pk=request.user.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

# TODO: static method
