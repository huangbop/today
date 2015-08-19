from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    is_show = serializers.BooleanField(default=False)
    is_pep = serializers.BooleanField(default=False)
    is_hot = serializers.BooleanField(default=False)
    is_new = serializers.BooleanField(default=False)

    class Meta:
        model = Product
