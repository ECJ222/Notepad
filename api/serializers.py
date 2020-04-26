from rest_framework import serializers
from .models import Notepad,Image
from django.contrib.auth.models import  User
from rest_framework.authtoken.models import Token
class NoteSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField('get_username')

     
    class Meta:
        model=Notepad
        fields=['id','title','username','user','editing']

    def get_username(self,notepad):
        user=notepad.username.username
        return user

class ImageSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField('get_username')

     
    class Meta:
        model=Image
        fields=['id','image','username','user','show']

    def get_username(self,image):
        user=image.username.username
        return user

class Userserializer(serializers.ModelSerializer):
    class Meta:
         model=User
         fields=('id','username','password')
         extra_kwargs={'password':{'write_only':True,'required':True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        print(user)
        Token.objects.create(user=user)
        return user
    
