from rest_framework.views import APIView
from rest_framework.response import Response
import hashlib, time
from utles.wx import wx_login
from django.core.cache import cache
from api.models import Address
from api.ser.user_ser import AddressModelSerializer
from rest_framework.generics import GenericAPIView


# class UserLogin(APIView):
#     def post(self, request):
#         param = request.data
#         if param.get('code'):
#             data = wx_login.login(param.get('code'))
#             if data:
#                 val = data['openid'] + '&' + data['session_key']
#                 key = data['openid'] + str(int(time.time()))
#                 md5 = hashlib.md5()
#                 md5.update(key.encode('utf-8'))
#                 key=md5.hexdigest()
#                 cache.set(key, val)
#                 user_obj = Address.objects.filter(open_id=data['openid']).first
#                 if not user_obj:
#                     Address.objects.create(open_id=data['openid'])
#                 send_msg = {
#                     'data': key
#                 }
#                 return Response(data=send_msg)
#             else:
#                 return Response('无效code')
#         return Response('无参数')



# 测试, 没用微信接口
class UserLogin(APIView):

    def post(self, request):
        param = request.data
        if param.get('code'):

            # data = wx_login.login(param.get('code'))
            data = {'openid': 'kjsfh1238bzct78aeg', 'session_key':'ahdsoyhxb327&e7*89fe27&Sqw34'}
            if data:
                val = data['openid'] + '&' + data['session_key']
                key = data['openid'] + str(int(time.time()))
                md5 = hashlib.md5()
                md5.update(key.encode('utf-8'))
                key=md5.hexdigest()
                cache.set(key, val, 100000000)
                user_obj = Address.objects.filter(open_id=data['openid']).first()
                if not user_obj:
                    Address.objects.create(open_id=data['openid'])
                send_msg = {
                    'data': key
                }
                return Response(data=send_msg)
            else:
                return Response('无效code')
        return Response('无参数')


class UserAddress(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        key = request_data.pop('key')
        if cache.get(key):
            openid = cache.get(key).split('&')[0]
            request_data['open_id'] = openid
            adr_ser = AddressModelSerializer(data=request_data)
            if adr_ser.is_valid():
                adr_ser.save()
                return Response(data={"success": True})
            else:
                return Response(data={"success": False})


class CheckAddress(APIView):
    def get(self, request, *args, **kwargs):
        request_data = request.data
        key = request_data.get('key')
        if cache.get(key):
            openid = cache.get(key).split("&")[0]
            user_adr_obj = Address.objects.filter(open_id=openid, is_delete=False).all()
            user_adr_ser = AddressModelSerializer(instance=user_adr_obj, many=True).data
            return Response(data=user_adr_ser)
        else:
            return Response(data={"msg": "未登录!"})














