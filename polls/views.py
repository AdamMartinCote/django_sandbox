"""
View

Each view is responsible for doing one of two things: returning an HttpResponse
object containing the content for the requested page, or raising an exception
such as Http404. The rest is up to you.

All Django wants is that HttpResponse. Or an exception.
"""
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
