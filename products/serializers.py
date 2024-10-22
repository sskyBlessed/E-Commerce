from rest_framework import serializers

def get_dynamic_serializer(CustomBaseProductModel):
    class DynamicSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomBaseProductModel
            fields = '__all__'
            
    return DynamicSerializer
