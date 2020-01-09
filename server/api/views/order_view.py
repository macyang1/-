from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Address, Food, BigOrder, SmallOrder
from api.ser.order_ser import BigOrderModelSerializer, SmallOrderModelSerializer
from api.ser.store_ser import FoodsModelSerializer


class ShopCar(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        key = request_data.get('key')
        if cache.get(key):
            openid = cache.get(key).split('&')[0]
            if cache.get(openid):
                send_dict = cache.get(openid)
                print(send_dict)
                return Response(data=send_dict)
            else:
                return Response(data={'msg':'空空如也'})
        else:
            return Response('未登录!')



class EditCar(APIView):
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
                # user_obj = Address.objects.filter(open_id=openid).first()
                food_obj = Food.objects.filter(pk=food_id).first()

                if not cache.get(openid):
                    food_ser = FoodsModelSerializer(instance=food_obj).data
                    order_dict = {
                        'foods': {
                            f'{food_ser["id"]}': {
                                "food_account": "",
                                "food_price": food_ser['price'],
                                "food_num": 1,
                                "food_name": food_ser["name"],
                                "food_id": food_ser["id"]
                            }
                        },
                        "status": '0'
                    }
                    cache.set(openid, order_dict)


                else:
                    order_dict = cache.get(openid)
                    print(order_dict['foods'])
                    if str(food_id) in order_dict['foods']:

                        if request_data.get('flag'):
                            order_dict['foods'][f'{food_id}']['food_num'] += 1
                        else:
                            order_dict['foods'][f'{food_id}']['food_num'] -= 1
                            if order_dict['foods'][f'{food_id}']['food_num'] <= 1:
                                order_dict['foods'][f'{food_id}']['food_num'] = 1
                                cache.set(openid, order_dict, 3600000)
                                return Response(data={"success": False})
                    cache.set(openid, order_dict, 3600000)
                print(cache.get(openid))
                return Response(data={"success": True})

            else:
                return Response('非法用户')


class CheckBefore(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        key = request_data.get('key')
        if cache.get(key):
            openid = cache.get(key).split('&')[0]
            user_befor_order = BigOrder.objects.filter(openid=openid).all()
            send_data = BigOrderModelSerializer(instance=user_befor_order, many=True).data
            print(send_data)
            if not user_befor_order:
                return Response('没有完成的订单')
            else:
                return Response('OK')


class DeleteFood(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        key = request_data.get('key')
        food_id = request_data.get('food_id')
        if cache.get(key):
            openid = cache.get(key).split("&")[0]
            cache.get(openid)['foods'].pop(str(food_id))
            return Response(data={'success': True})
        else:
            return Response(data={"mag": '未登录!'})


