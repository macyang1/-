from api.models import BigOrder, SmallOrder, Active
from rest_framework.serializers import ModelSerializer


class BigOrderModelSerializer(ModelSerializer):

    class Meta:
        model = BigOrder
        fields = ('open_id', 'order_id', 'status', 'address', 'small_order')


class SmallOrderModelSerializer(ModelSerializer):

    class Meta:
        fields = ('food_id', 'is_discount')





















