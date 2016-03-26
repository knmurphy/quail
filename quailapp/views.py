from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

import datetime

from .forms import QuestionForm
from .models import Question

def index(request):
    return render(request, 'index.html', {'questions': Question.objects.all()})

def get_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_question = Question(created_on=datetime.datetime.now(), text=data['your_question'], votes=0)
            new_question.save()
            return redirect('/')
    else:
        form = QuestionForm()
    return render(request, 'question.html', {'form': form})

def delete_questions(request):
    Question.objects.all().delete()
    return HttpResponse('All questions have been deleted!')

def hello_world(request):
    return HttpResponse('Hello world!')
