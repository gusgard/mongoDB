from django.http import HttpResponse
from prueba.models import Poll, Choice
from django.shortcuts import render_to_response


#user = authenticate(username='user', password='user')
from datetime import datetime

def index(request):
    fecha = datetime.now()
    poll = Poll(question="What2", pub_date=fecha)
    choice = Choice(choice_text="I'm at DjangoCon.fi2", votes=23)
    poll.choices.append(choice)
    poll.save()
    print poll.question
    return render_to_response('charts.html')
    #return HttpResponse("Hello, world. You're at the poll index.")


def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)