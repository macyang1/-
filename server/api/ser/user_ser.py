from rest_framework.serializers import ModelSerializer
from api import models





class AddressModelSerializer(ModelSerializer):

    class Meta:
        model = models.Address
        fields = ('name', 'phone', 'address', 'open_id')














