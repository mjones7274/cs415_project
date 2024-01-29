from django.http import JsonResponse
from cs415.models import User, Useraddress, Userphone, Phonetype, Userinfo, Pagedata, Addresstype
from cs415.serializers import UserSerializer, AddressSerializerPost, AddressSerializerGet, PhoneSerializerGet, PhoneSerializerPost
from cs415.serializers import PhoneTypeSerializer, UserinfoSerializer, PageDataSerializer, AddressTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
        return JsonResponse({'users': serializer.data})

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
        return JsonResponse(user_data)

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
        return JsonResponse({'user_addresses': serializer.data})

class UserAddressAPIView(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        addresses = Useraddress.objects.filter(user=user)
        serializer = AddressSerializerGet(addresses, many=True)
        return JsonResponse({'addresses': serializer.data})

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
        return JsonResponse({'user_phones': serializer.data})

class UserPhoneAPIView(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        phones = Userphone.objects.filter(user=user)
        serializer = PhoneSerializerGet(phones, many=True)
        return JsonResponse({'phones': serializer.data})

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
        return JsonResponse({'phone_types': serializer.data})

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
        return JsonResponse({'address_types': serializer.data})

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
        return JsonResponse({'user_infos': serializer.data})

class GetSingleUserInfoAPIView(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        info = Userinfo.objects.filter(user=user)
        serializer = UserinfoSerializer(info, many=True)
        return JsonResponse({'info': serializer.data})

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
        return JsonResponse({'pages': serializer.data})

class GetSinglePageDataAPIView(APIView):
    def get(self,request,id):
        page = Pagedata.objects.get(pk=id)
        serializer = PageDataSerializer(page)
        return JsonResponse(serializer.data)
