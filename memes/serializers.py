from rest_framework import serializers
from .models import Meme


# same thing but can be referenced by url
# class MemeSerializer(serializers.HyperlinkedModelSerializer):
class MemeSerializer(serializers.ModelSerializer):
    # TODO: whats wrong
    # url = serializers.HyperlinkedIdentityField("memes/<int:pk>/")
    extra_serializer_field = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Meme
        fields = ["id", "user", "name", "joke",
                  "description", "extra_serializer_field"]

    def get_extra_serializer_field(self, obj):
        return len(obj.name)
