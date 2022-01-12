from rest_framework import generics
from rest_framework.views import APIView
from quiz.models import Question, Quizzes
from quiz.serializers import AllQuizSerializer, AllQustionSerializer, QustionSerializer
from rest_framework.response import Response
from quiz.permissions import IsOwnerOrReadOnlyQueston


class AllQuiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = AllQuizSerializer



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


