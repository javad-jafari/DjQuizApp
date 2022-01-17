from email.mime import image
from quiz.models import Answer, Quizzes , Question
from rest_framework import serializers
from django.contrib.auth import get_user_model
from quiz.models import Question
User = get_user_model()



class QustionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
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

        technique =validated_data.pop('get_technique_display')
        difficulty=validated_data.pop('get_difficulty_display')

        obj = Question.objects.create(
            technique = technique,
            difficulty = difficulty,
            **validated_data
            )

        return obj



class AllQuizSerializer(serializers.ModelSerializer):

    question = QustionSerializer(many = True)
    class Meta:
        model = Quizzes
        fields ='__all__'

class QuizCreatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        exclude =("creator",)
    
    def create(self, validated_data):

        user = self.context["request"].user
        instance = self.Meta.model(**validated_data)
        instance.creator = user
        instance.save()

        return instance






class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ["password","username"]







class RegisterSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields =["username", "password","confirm_password"]

        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self,data):

        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password confirme is incorrect")

        if len(data["password"]) < 5:
            raise serializers.ValidationError("password len must be bigger than 5")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        validated_data.pop('confirm_password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance




class AdminRegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields =["username", "password", "confirm_password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    

    def validate(self,data):

        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password confirme is incorrect")

        if len(data["password"]) < 5:
            raise serializers.ValidationError("password len must be bigger than 5")
        return data

    def create(self, validated_data):
            password = validated_data.pop('password',None)
            validated_data.pop('confirm_password',None)

            instance = self.Meta.model(**validated_data)

            if password is not None:
                instance.set_password(password)
            
            instance.is_staff = True
            instance.is_superuser = True
            instance.save()

            return instance

