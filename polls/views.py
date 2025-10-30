from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_questions = Question.objects.all()
    output = ', '.join([q.question_text for q in latest_questions])
    return HttpResponse("Latest questions: " + output)
