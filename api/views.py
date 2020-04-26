from django.shortcuts import render
from .models import Notepad,Image
from .serializers import NoteSerializer,Userserializer,ImageSerializer
from django.http import Http404
from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import  User
from rest_framework.authtoken.models import Token
from django.core import serializers

# Create your views here.
class NoteCRUD(viewsets.ModelViewSet):
    queryset=Notepad.objects.all()
    serializer_class=NoteSerializer
    permission_classes=(AllowAny,)
    authentication_classes=(TokenAuthentication,)

class UserAuth(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=Userserializer
    permission_classes=(AllowAny,)
    for user in queryset:
        Token.objects.get_or_create(user=user)


class ImageCRUD(viewsets.ModelViewSet):
    queryset=Image.objects.all()
    serializer_class=ImageSerializer
    permission_classes=(AllowAny,)
    authentication_classes=(TokenAuthentication,)
        
