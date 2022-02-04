import pdb
from rest_framework import serializers
from django.contrib.auth.models import User

from example.models import Product

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']


class ProductSerializer(serializers.ModelSerializer):

    cpu_company = serializers.ChoiceField(choices=Product.CPU_COMPANY_CHOICE)
    ram = serializers.ChoiceField(choices=Product.RAM_CHOICE)
    secondary_memory = serializers.ChoiceField(choices=Product.SECONDARY_MEMORY_CHOICE)
    secondary_storage = serializers.ChoiceField(choices=Product.SECONDARY_STORAGE_CHOICE)
    external_cooling = serializers.BooleanField()

    
    class Meta:
        model = Product
        fields = ['id','cpu_company','ram', 'secondary_memory', 'secondary_storage', 'external_cooling', 'case', 'psu', 'motherboard']