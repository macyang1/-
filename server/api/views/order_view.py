from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Address, Food, BigOrder, SmallOrder
# from api.ser.order_ser import


class ShopCar(APIView):
    '''
    kjsfh1238bzct78aeg
    '''
    def post(self, request, *args, **kwargs):
        request_data = request.data
        if request_data:
            key = request_data.get('key')
            food_id = request_data.get('food_id')
            if cache.get(key):
                openid = cache.get(key).split('&')[0]
                user_obj = Address.objects.filter(open_id=openid).first()
                food_obj = Food.objects.filter(pk=food_id).first()
                if not cache.get(openid):

                    if user_obj and food_obj:
                        order_dict = {}
                        order_dict[food_id] = {
                            'food_name': food_obj.name,
                            'food_price': food_obj.price,
                            'count': 1,
                        }

                        cache.set(openid, order_dict)
                        return Response(data=order_dict)
                    else:
                        return Response('用户/商品不存在')
                else:
                    order_dict = cache.get(openid)
                    if food_id in order_dict:
                        if request_data.get('flag'):
                            order_dict[food_id]['count'] += 1
                        else:
                            order_dict[food_id]['count'] -= 1
                            if order_dict[openid]['count'] < 1:
                                order_dict.pop(food_id)
                    else:
                        if user_obj and food_obj:
                            order_dict = {}
                            order_dict[food_id] = {
                                'food_name': food_obj.name,
                                'food_price': food_obj.price,
                                'count': 1,
                            }
                        cache.set(openid, order_dict)
                    return Response(data=order_dict)

            else:
                return Response('非法用户')


class CheckBefore(APIView):
    def pots(self, request, *args, **kwargs):
        request_data = request.data
        key = request_data.get('key')
        if cache.get(key):
            openid = cache.get(key).split('&')[0]
            user_befer_order = BigOrder.objects.filter(openid=openid).all()
            if not user_befer_order:
                return Response('没有完成的订单')
            else:
                for big_order in user_befer_order:
                    small_order_list = SmallOrder.objects.filter(big_order=big_order.id).all()
                    for smll_order in small_order_list:

                        pass




