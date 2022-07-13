from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, attrs):
        title = attrs.get('title')
        title = title.upper()
        attrs['title'] = title
        print(title)
        return attrs

    def validate_description(self, d):
        if len(d) < 20:
            raise serializers.ValidationError('Опиание слишком короткое')

        return d
