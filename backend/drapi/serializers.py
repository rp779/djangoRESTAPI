from rest_framework import serializers
from .models import Drapi

# subclass the Model serializer and add a
# Meta class. The Meta class defines what model
# will be serialized and which fields to expose
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drapi
        # id is created automatically by django!
        fields = ("id", "title", "body")
