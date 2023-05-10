from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount= serializers.SerializerMethodField(read_only=True)
    url= serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only = True)
    class Meta:
        model = Product
        fields= [
            'url',
            'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    title = serializers.CharField(validators=[validators.validate_title_nohello, validators.unique_product_title])
    def create(self, validated_data):
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        print(email, obj)
        return obj
        
    
    def get_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("update_view", kwargs={"pk": obj.pk}, request=request)
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        # try:
        #     return obj.get_discount()
        # except:
        #     return None