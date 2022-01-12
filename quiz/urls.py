from django.contrib import admin
from django.urls import path
from quiz.views import AllQuiz, AllQustion, QustionDetail, RandomQuestion
urlpatterns = [
    path('quizes', AllQuiz.as_view(), name='quizes' ),
    path('questions', AllQustion.as_view(), name='questions' ),
    path('randomquestion', RandomQuestion.as_view(), name='randomquestion' ),
    path('question/<int:pk>', QustionDetail.as_view(), name='question-detail' ),

]
