from quiz.models import Answer, Quizzes , Question
from rest_framework import serializers


class QustionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class AllQuizSerializer(serializers.ModelSerializer):

    question = QustionSerializer(many = True)
    class Meta:
        model = Quizzes
        fields = '__all__'

class AllQustionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


    quze_of = serializers.StringRelatedField(source='quiz')
    answer = AnswerSerializer(many = True, read_only=True)
    technique = serializers.CharField(source='get_technique_display')
    difficulty = serializers.CharField(source='get_difficulty_display')

    def create(self, validated_data):
  
        obj = Question.objects.create(
            technique = validated_data['get_technique_display'],
            difficulty = validated_data['get_technique_display'],
            title = validated_data['title'],
            is_active = validated_data['is_active'],
            quiz = validated_data['quiz']
            )
        return obj
        