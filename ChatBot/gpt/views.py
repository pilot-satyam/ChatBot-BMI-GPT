from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .utils import get_recommendations,calculate_bmi

class UserView(APIView):
    def post(self, request):
        height = request.data.get('height')
        weight = request.data.get('weight')
        bmi = calculate_bmi(height, weight)
        bmi,diet_recommendations, exercise_recommendations, test_recommendations = get_recommendations(bmi)
        user = User.objects.create(height=height, weight=weight, bmi=bmi, diet_recommendations=diet_recommendations, exercise_recommendations=exercise_recommendations, test_recommendations=test_recommendations)
        return Response({
            'height': user.height,
            'weight': user.weight,
            'bmi': user.bmi,
            'diet_recommendations': user.diet_recommendations,
            'exercise_recommendations': user.exercise_recommendations,
            'test_recommendations': user.test_recommendations,
        })

