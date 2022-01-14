from rest_framework import generics
from rest_framework.views import APIView
from quiz.models import Question, Quizzes
from quiz.serializers import (AllQuizSerializer,
AllQustionSerializer, QuizCreatorSerializer,
RegisterSerializer, UserSerializer, AdminRegisterSerializer,)
from rest_framework.response import Response
from quiz.permissions import IsOwnerOrReadOnlyQueston, IsAdminOrOwnerOrReadOnly
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication


User = get_user_model()

class AllQuiz(generics.ListCreateAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = AllQuizSerializer



class QuizCreateApi(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = Quizzes.objects.all()
    serializer_class = QuizCreatorSerializer


class AllQustion(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnlyQueston]
    queryset = Question.objects.all()
    serializer_class = AllQustionSerializer



class QustionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnlyQueston]
    queryset = Question.objects.all()
    serializer_class = AllQustionSerializer




class RandomQuestion(APIView):
    
    def get(self, requset, format=None):
        random = Question.objects.all().order_by('?').first()
        serializer = AllQustionSerializer(random)
        return Response(serializer.data)




class UserApi(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer




class UserDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer




class Register(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer




class AdminRegister(generics.CreateAPIView):

    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = AdminRegisterSerializer


