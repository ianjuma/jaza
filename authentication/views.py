import json
from django.contrib.auth import login, logout, authenticate
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from authentication.permissions import IsAccountOwner
from authentication.serializers import UserSerializer


class Login(views.APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username', None)
        password = data.get('password', None)
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


class AuthView(views.APIView):
    """
    sample view
    Authentication is needed for this methods -- apply permissions across the API
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'detail': "I suppose you are authenticated"})


class AuthToken(views.APIView):
    def get(self):
        return Response({'GET': 'GET RESPONSE'})

    def post(self, request):
        try:
            data = request.DATA
        except ParseError:
            return Response({'Invalid': 'Bad Input'}, status=status.HTTP_400_BAD_REQUEST)

        if 'user' not in data or 'password' not in data:
            return Response({'Invalid': 'Bad Input'}, status=status.HTTP_400_BAD_REQUEST)

        # check is pass and username match
        # then store token
        # won't get token
        user = User.objects.first()

        if not user:
            return Response({'Error': 'No default User'}, status=status.HTTP_404_NOT_FOUND)

        token = Token.objects.get_or_create(user=user)
        return Response({'token': token[0].key}, status=status.HTTP_201_CREATED)


class Logout(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return permissions.IsAuthenticated(), IsAccountOwner()

    def list(self, request):
        queryset = self.queryset.filter(pk=request.user.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# TODO: login / logout view
# TODO: static method
