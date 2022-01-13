from django.urls import path
from quiz.views import (AdminRegister,
AllQuiz, AllQustion, QuizCreateApi,
QustionDetail, RandomQuestion, Register,
UserApi, UserDetailApi)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('quizes', AllQuiz.as_view(), name='quizes' ),
    path('creatquize', QuizCreateApi.as_view(), name='create-quizes' ),
    path('questions', AllQustion.as_view(), name='questions' ),
    path('randomquestion', RandomQuestion.as_view(), name='randomquestion' ),
    path('question/<int:pk>', QustionDetail.as_view(), name='question-detail' ),
    path('user/<int:pk>', UserDetailApi.as_view(), name='user-detail' ),
    path('users', UserApi.as_view(), name='users' ),
    path('register', Register.as_view(), name='register' ),
    path('adminregister', AdminRegister.as_view(), name='adminregister' ),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
