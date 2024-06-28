from rest_framework import serializers

from customer.models import Stock


# to transfer objects over network (db server), we need to serialize the object
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
