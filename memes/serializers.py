from rest_framework import serializers
from .models import Meme


class MemeSerializer(serializers.ModelSerializer):
    extra_serializer_field = serializers.SerializerMethodField(read_only=True)
    class Meta():
        model = Meme
        fields = ["id", "name", "joke", "description", "extra_serializer_field"]

    def get_extra_serializer_field(self, obj):
        return len(obj.name)
