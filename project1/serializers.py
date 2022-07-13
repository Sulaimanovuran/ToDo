from rest_framework import serializers
from project1.models import BuyProduct


class BuyProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = BuyProduct
        fields = '__all__'

    def validate(self, attrs):
        title = attrs.get('title')
        title = title.title()
        attrs['title'] = title
        return attrs

    def validate_description(self, d):
        if len(d) > 30:
            raise serializers.ValidationError("Описание слишком длинное")
        return d
