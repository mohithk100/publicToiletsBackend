from rest_framework import serializers
from user_accounts.models import User
from django.http import JsonResponse
from twilio.rest import Client
import random
import urllib2
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','mobileNumber','avatar')

class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
		style={'input_type': 'password'},
		write_only=True)
    type_of_request = serializers.CharField(max_length = 20 , required = True,write_only = True)
    success = serializers.CharField(required=False)
    message = serializers.CharField(required = False)
    otp = serializers.IntegerField(required = False)
    class Meta:
        model = User
        fields = (
                'username',
                'password',
                'email',
                'first_name',
                'last_name',
                'mobileNumber',
                'avatar' ,
                'type_of_request',
                'success',
                'message',
                'otp',
                )

    def create(self , validated_data):
        request = self.context.get('request')
        type_of_request = validated_data['type_of_request']
        if type_of_request == 'request_otp':
            auth_token = '1729bdc3c04616dbc8ca2a1fde8b5a46'
            account_sid = 'ACf5adb3a8c7f5bfbffb575a2837e707f4'
            otp = random.randint(100000,999999)
            twilio_number = "+16304746450"
            to_number = "+91"+str(validated_data['mobileNumber'])
            body = "Welcome To Public Toilets. Your verification code is :" + str(otp)
            client = Client(account_sid , auth_token)
            message = client.api.messages.create(to_number,
                                                from_=twilio_number,
                                                body = body)
            if message.sid:
                validated_data['success'] = True
                validated_data['message'] = "OTP sent successfully"
                validated_data['otp'] = otp
            else:
                validated_data['success'] = False
                validated_data['message'] = "OTP sending Failed"
            print validated_data
            return validated_data

        elif type_of_request == 'register_user':
            list_of_keys = validated_data.keys()
            user = User(
                username = validated_data.pop('username'),
                mobileNumber = validated_data.pop('mobileNumber'), #making mobile number required
            )
            user.set_password(validated_data.pop('password'))
            if ('email' in list_of_keys):
                user.email = validated_data.pop('email')
            if ('first_name' in list_of_keys):
                user.first_name = validated_data.pop('first_name')
            if ('last_name' in list_of_keys):
                user.last_name = validated_data.pop('last_name')
            if ('avatar' in list_of_keys):
                user.avatar = validated_data.pop('avatar')
            user.save()
            return user




class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','mobileNumber','avatar')
