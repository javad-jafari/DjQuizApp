from rest_framework import generics
from rest_framework.views import APIView
from quiz.models import Question, Quizzes
from quiz.serializers import AllQuizSerializer, AllQustionSerializer, QustionSerializer
from rest_framework.response import Response
from rest_framework import permissions
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



class AllQuiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = AllQuizSerializer



class AllQustion(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = AllQustionSerializer



class QustionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = AllQustionSerializer




class RandomQuestion(APIView):
    
    def get(self, requset, format=None):
        random = Question.objects.all().order_by('?').first()
        serializer = AllQustionSerializer(random)
        return Response(serializer.data)


