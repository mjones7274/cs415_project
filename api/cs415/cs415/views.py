from django.http import JsonResponse
import json
import sys
from cs415.models import User, Useraddress, Userphone, Phonetype, Userinfo, Pagedata, Addresstype
from cs415.serializers import UserSerializer, AddressSerializer, PhoneSerializer
from cs415.serializers import PhoneTypeSerializer, UserinfoSerializer, PageDataSerializer, AddressTypeSerializer


def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'users': serializer.data})

def address_list(request):
    user_addresses = Useraddress.objects.all()
    serializer = AddressSerializer(user_addresses, many=True)
    return JsonResponse({'user_addresses': serializer.data})

def phone_list(request):
    user_phones = Userphone.objects.all()
    serializer = PhoneSerializer(user_phones, many=True)
    return JsonResponse({'user_phones': serializer.data})

def phonetype_list(request):
    phone_types = Phonetype.objects.all()
    serializer = PhoneTypeSerializer(phone_types, many=True)
    return JsonResponse({'phone_types': serializer.data})

def addresstype_list(request):
    address_types = Addresstype.objects.all()
    serializer = AddressTypeSerializer(address_types, many=True)
    return JsonResponse({'address_types': serializer.data})

def userinfo_list(request):
    user_infos = Userinfo.objects.all()
    serializer = UserinfoSerializer(user_infos, many=True)
    return JsonResponse({'user_infos': serializer.data})

def pagedata_list(request):
    page_datas = Pagedata.objects.all()
    serializer = PageDataSerializer(page_datas, many=True)
    return JsonResponse({'pages': serializer.data})

def user(request, id):
    user = User.objects.get(pk=id)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

def user_address(request, id):
    user = User.objects.get(pk=id)
    addresses = Useraddress.objects.filter(user=user)
    serializer = AddressSerializer(addresses, many=True)
    return JsonResponse({'addresses': serializer.data})

def user_phone(request, id):
    user = User.objects.get(pk=id)
    phones = Userphone.objects.filter(user=user)
    serializer = PhoneSerializer(phones, many=True)
    return JsonResponse({'phones': serializer.data})

def user_info(request, id):
    user = User.objects.get(pk=id)
    info = Userinfo.objects.filter(user=user)
    serializer = UserinfoSerializer(info, many=True)
    return JsonResponse({'info': serializer.data})

def user(request, id):
    user = User.objects.get(pk=id)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

def pagedata(request, id):
    page = Pagedata.objects.get(pk=id)
    serializer = PageDataSerializer(page)
    return JsonResponse(serializer.data)

def user_data(request, id):
    user_data = {}
    user = User.objects.get(pk=id)
    user_serial = UserSerializer(user)
    user_data.update({"user": user_serial.data})
    addresses = AddressSerializer(Useraddress.objects.filter(user=user), many=True)
    user_data.update({"addresses": addresses.data})
    info = UserinfoSerializer(Userinfo.objects.filter(user=user), many=True)
    user_data.update({"info": info.data})
    phone = PhoneSerializer(Userphone.objects.filter(user=user).select_related(), many=True)
    user_data.update({"phones": phone.data})
    return JsonResponse(user_data)