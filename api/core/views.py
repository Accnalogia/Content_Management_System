from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer, LoginSerializer
from .models import CMSUser
from .utils import user_detail
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist


class RegisterViewset(viewsets.ModelViewSet):
    queryset = CMSUser.objects.all()
    serializer_class = RegisterSerializer

    def post_register(self, request):
        email = request.data.get("email")
        queryset = CMSUser.objects.filter(email=email)
        if queryset is not None and len(queryset) > 0:
            return Response(status=status.HTTP_409_CONFLICT, data={"User already registered."})

        ser = RegisterSerializer(
            data=request.data, context={'request': request}
        )
        if ser.is_valid():
            try:
                user = ser.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                response = user_detail(user)
                return Response(response, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                return Response(
                    {'reason': "Invalid Login"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        return Response(
            {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)


class LoginViewset(viewsets.ModelViewSet):
    queryset = CMSUser.objects.all()
    serializer_class = LoginSerializer

    def post_login(self, request):
        ser = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if ser.is_valid(raise_exception=True):
            user = ser.validated_data['user']
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                response = user_detail(user)
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED, data={"Login Failed! Please Try again"})

