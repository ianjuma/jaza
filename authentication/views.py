import json
from django.contrib.auth import login, logout, authenticate
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

# token auth
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer


class Login(views.APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active():
                login(request, user)
                serialized = AccountSerializer(user)
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
        user = Account.objects.first()

        if not user:
            return Response({'Error': 'No default User'}, status=status.HTTP_404_NOT_FOUND)

        token = Token.objects.get_or_create(user=user)
        return Response({'token': token[0].key}, status=status.HTTP_201_CREATED)


class Logout(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return permissions.AllowAny()

        if self.request.method == 'POST':
            return permissions.AllowAny()

        return permissions.IsAuthenticated(), IsAccountOwner()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({'status': 'Bad request',
                         'message': 'Account could not be created with received data.'},
                        status=status.HTTP_400_BAD_REQUEST)


# TODO: login / logout view
# TODO: static method
