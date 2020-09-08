from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerialazer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    fist_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

    def create(self, validate_data):
        instance=User()
        instance.fist_name=validate_data.get('fist_name')
        instance.last_name= validate_data.get('last_name')
        instance.username=validate_data.get('username')
        instance.email=validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance


    def validate_user(self,data):
        users= User.objects.filter(username= data)
        if len(users)!=0:
            raise serializers.ValidationError("este usuario ya existe ingrese uno nuevo")
        else:
            return data











