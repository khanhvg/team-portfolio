from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'memo', 'created', 'datecompleted', 'important')
        extra_kwargs = {'user': {'read_only': True}}
