import csv  # https://docs.python.org/3/library/csv.html

from polls.models import Question, Choice
from django.utils import timezone

def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    fhand = open('scripts/dj4e_batch.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:
        print(row)

        # Make a new Question and save it
        q = Question(question_text = row[0], pub_date = timezone.now())
        q.save()
        print(q)
        # Loop through the choice strings in row[1:] and add each choice,
        for c in row[1:]:
            q.choice_set.create(choice_text = c)
        # connect it to the question and save it

    print("=== Load Complete")