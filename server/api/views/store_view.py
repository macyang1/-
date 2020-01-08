from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Food, FoodDetail, Category, Warehouse
from api.ser.store_ser import FoodsModelSerializer, CategoryModelSerializer, FoodDetailModelSerializer
from django.core.cache import cache

from django.http import JsonResponse


category_dict = {
    '1': '荤菜',
    '2': '素菜',
    '3': '甜点',
    '4': '鲜汤'
}



class FoodInfo(APIView):
    def get(self, request, *args, **kwargs):
        cat_data = Category.objects.all()
        data_list = CategoryModelSerializer(instance=cat_data, many=True, context={'request': request}).data

        return Response(data=data_list)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        if request_data.get('food_id'):
            food_obj = Food.objects.filter(pk=request_data.get('food_id')).first()
            food_detail_obj = FoodDetail.objects.filter(id=food_obj.detail_id).first()
            food_detail_ser = FoodDetailModelSerializer(instance=food_detail_obj).data
            print(food_detail_ser)
            food_ser = FoodsModelSerializer(instance=food_obj).data
            send_msg = {}
            send_msg['food_id'] = food_ser['id']
            send_msg['food_name'] = food_ser['name']
            send_msg['food_price'] = food_ser['price']
            send_msg['img'] = food_ser['img']
            send_msg['food_detail'] = {
                'food_dec': food_detail_ser['dec']
            }
            return Response(data=send_msg)
        else:
            return Response('非法请求!')



















