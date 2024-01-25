from rest_framework import serializers
from cs415.models import User, Useraddress, Userinfo, Userphone, Phonetype, Pagedata, Addresstype

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['user_id', 'first_name', 'last_name', 'email' , 'pass_word', 'created_date', 'is_active']
        fields = '__all__'

class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addresstype
        depth=1
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    address_type = AddressTypeSerializer(read_only=True)
    class Meta:
        model = Useraddress
        # depth = 1
        fields = '__all__'

class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phonetype
        depth=1
        fields = '__all__'

class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addresstype
        depth=1
        fields = '__all__'

class PhoneSerializer(serializers.ModelSerializer):
    phone_type = PhoneTypeSerializer(read_only=True)
    class Meta:
        model=Userphone
        fields = '__all__'

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userinfo
        fields='__all__'

class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagedata
        fields='__all__'
