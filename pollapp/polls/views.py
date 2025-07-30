from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def add_poll(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        options = request.POST.getlist('options')
        if question_form.is_valid():
            question = question_form.save()
            for opt_text in options:
                if opt_text.strip():
                    Option.objects.create(question=question, text=opt_text)
            return redirect('index')
    else:
        question_form = QuestionForm()
    return render(request, 'add_poll.html', {'question_form': question_form})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        option_id = request.POST.get('option')
        option = get_object_or_404(Option, pk=option_id)
        option.votes += 1
        option.save()
        return redirect('results', question_id=question.id)
    return render(request, 'vote.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})
