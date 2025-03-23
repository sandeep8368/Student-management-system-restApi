from rest_framework import serializers
from app.models import studentModel

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'