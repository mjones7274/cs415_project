from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Useraddress, Userphone, Phonetype, Userinfo, Pagedata, Addresstype
from cs415.serializers import UserSerializer, AddressSerializerPost, AddressSerializerGet, PhoneSerializerGet, PhoneSerializerPost
from cs415.serializers import PhoneTypeSerializer, UserinfoSerializer, PageDataSerializer, AddressTypeSerializer
from django.contrib.auth import login
import datetime
import jwt


class UserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

class PageDataAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PageDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        page_datas = Pagedata.objects.all()
        serializer = PageDataSerializer(page_datas, many=True)
        return Response({'pages': serializer.data})

class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)

        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                             status=status.HTTP_404_NOT_FOUND)

        check_pass = User.objects.filter(email = email, pass_word=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email = email, pass_word=password)
        if user is not None:
            login(request, user)
            token = {
                "user_id": user.user_id,
                "scope": 'admin',
                "first_name": user.first_name,
                "last_name": user.last_name,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8),
                "iat": datetime.datetime.utcnow()
            }
            key = 'valhalla'
            jwt_token = jwt.encode(token, key=key, algorithm="HS256")
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'token': jwt_token},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_BAD_REQUEST)


class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        user_data = {}
        user = User.objects.get(pk=id)
        user_serial = UserSerializer(user)
        user_data.update({"user": user_serial.data})
        addresses = AddressSerializerGet(Useraddress.objects.filter(user=user), many=True)
        user_data.update({"addresses": addresses.data})
        info = UserinfoSerializer(Userinfo.objects.filter(user=user), many=True)
        user_data.update({"info": info.data})
        phone = PhoneSerializerGet(Userphone.objects.filter(user=user).select_related(), many=True)
        user_data.update({"phones": phone.data})
        return Response(user_data)

class AddressAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AddressSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        user_addresses = Useraddress.objects.all()
        serializer = AddressSerializerGet(user_addresses, many=True)
        return Response({'user_addresses': serializer.data})

class UserAddressAPIView(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        addresses = Useraddress.objects.filter(user=user)
        serializer = AddressSerializerGet(addresses, many=True)
        return Response({'addresses': serializer.data})

class PhoneAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PhoneSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        user_phones = Userphone.objects.all()
        serializer = PhoneSerializerGet(user_phones, many=True)
        return Response({'user_phones': serializer.data})

class UserPhoneAPIView(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        phones = Userphone.objects.filter(user=user)
        serializer = PhoneSerializerGet(phones, many=True)
        return Response({'phones': serializer.data})

class PhoneTypeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PhoneTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        phone_types = Phonetype.objects.all()
        serializer = PhoneTypeSerializer(phone_types, many=True)
        return Response({'phone_types': serializer.data})

class AddressTypeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AddressTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        address_types = Addresstype.objects.all()
        serializer = AddressTypeSerializer(address_types, many=True)
        return Response({'address_types': serializer.data})

class UserInfoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserinfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        user_infos = Userinfo.objects.all()
        serializer = UserinfoSerializer(user_infos, many=True)
        return Response({'user_infos': serializer.data})

class GetSingleUserInfoAPIView(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        info = Userinfo.objects.filter(user=user)
        serializer = UserinfoSerializer(info, many=True)
        return Response({'info': serializer.data})

class GetSinglePageDataAPIView(APIView):
    def get(self,request,id):
        page = Pagedata.objects.get(pk=id)
        serializer = PageDataSerializer(page)
        return Response({'page': serializer.data})
