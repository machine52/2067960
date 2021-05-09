from rest_framework import serializers
from home.models import *

class producto_serializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = producto
        fields = ('url', 'nombre' , 'descripcion', 'precio','cantidad','activo','foto', 'marca','categoria',)

class marca_serializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url', 'nombre' ,)

class categoria_serializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre',)        