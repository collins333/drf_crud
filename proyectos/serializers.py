from rest_framework import serializers
from .models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Proyecto
    fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'creado')
    read_only_fields = ('creado',)