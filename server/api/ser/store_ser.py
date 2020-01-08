from rest_framework.serializers import ModelSerializer
from api import models


class FoodsModelSerializer(ModelSerializer):

    class Meta:
        model = models.Food
        fields = ['id', 'name', 'price', 'detail', 'category', 'img', 'detail']


class FoodDetailModelSerializer(ModelSerializer):

    class Meta:
        model = models.FoodDetail
        fields = ['sale_num', 'ingredient', 'dec']


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name', 'foods', 'id']


class WarehouseModelSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['num', 'food']


