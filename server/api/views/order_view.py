from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Address, Food




class ShopCar(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        if request_data:
            key = request_data.get('key')
            food_id = request_data.get('food_id')
            if cache.get(key):
                openid = cache.get('key').split('&')[0]
                if not cache.get(openid):
                    user_obj = Address.objects.filter(open_id=openid).first()
                    food_obj = Food.objects.filter(pk=food_id).first()
                    if user_obj and food_obj:
                        order_dict = {openid:[]}
                        food_dict = {
                            'food_name': food_obj.name,
                            'food_price': food_obj.price,
                            'count': 1,
                        }
                        order_dict[openid].append(food_dict)

                        cache.set(openid, order_dict)
                        return Response(data=order_dict)
                    else:
                        return Response('用户/商品不存在')
                else:
                    order_dict = cache.get(openid)
                    if request_data.get(food_id) in order_dict[openid].values():
                        if request_data.get('flag'):
                            order_dict[openid]['count'] += 1
                        else:
                            order_dict[openid]['count'] -= 1


                        cache.set(openid, order_dict)
                    return Response('添加成功')

            else:
                return Response('非法用户')
























