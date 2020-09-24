from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Survey, Questions, Answer
from .serializers import SurveySerializer, UserSerializer, QuestionSerializer, AnswerSerializer

class SurveyView(APIView):
    def get(self, request):
        survies = Survey.objects.all()
        serializer = SurveySerializer(survies, many=True)
        return Response({"Опросы": serializer.data})

    def post(self, request):
        survey = request.data.get('survey')
        serializer = SurveySerializer(data=survey)
        if serializer.is_valid(raise_exception=True):
            survey_saved = serializer.save()
        return Response({"Опрос '{}' успешно создан".format(survey_saved)})

    def put(self, request, pk):
        saved_survey = get_object_or_404(Survey.objects.all(), pk=pk)
        data = request.data.get('survey')
        serializer = SurveySerializer(instance=saved_survey, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            survey_saved = serializer.save()
        return Response({
            "Опрос '{}' успешно оьновлен".format(survey_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        survey = get_object_or_404(Survey.objects.all(), pk=pk)
        survey.delete()
        return Response({
            "Опрос `{}` успешно удален.".format(pk)
        }, status=204)


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"Пользователи": serializer.data})


class QuestionsView(APIView):
    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response({"Вопросы": serializer})


class AnswerView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response({"Ответы": serializer})
