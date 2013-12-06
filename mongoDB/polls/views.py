from polls.models import Poll, Choice

poll = Poll.objects(question__contains="What").first()
choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
poll.choices.append(choice)
poll.save()

print poll.question