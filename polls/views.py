from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Question, Choice
# Create your views here.
def index(request):
    questions = Question.objects.order_by("-pub_date")[0:]
    title = "Home"
    context = {"questions":questions, "title" : title}
    return render(request, "polls/index.html", context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {"question": question, "title": "details", "choices": choices}
    return render(request, "polls/details.html", context)

def results(request, question_id):
    response = f"You are looking for results for {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")