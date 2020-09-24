from rest_framework import serializers

from surveyusers.models import Survey, Questions, Answer, User


class SurveySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    description = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        return Survey.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance


class QuestionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    description = serializers.CharField()

    def create(self, validated_data):
        return Questions.object.create(**validated_data)


class AnswerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    answer = serializers.CharField()

    def create(self, validated_data):
        return Answer.object.create(**validated_data)


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return User.object.create(**validated_data)


