from rest_framework import serializers # type: ignore
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # El modelo que se va a serializar
        fields = ('id', 'name', 'email', 'gender')