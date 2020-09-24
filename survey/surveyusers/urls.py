from django.urls import path
from .views import SurveyView, UserView, QuestionsView, AnswerView

app_name = "survey"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', UserView.as_view()),
    path('survey/', SurveyView.as_view()),
    path('survey/<int:pk>', SurveyView.as_view()),
    path('questions/', QuestionsView.as_view()),
    path('answers/', AnswerView.as_view()),
]
