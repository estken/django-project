from django.shortcuts import render
from .models import Grading_Results
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    if request.method == 'POST':
        Question = request.POST.get('Question')
        Choice_Field = request.POST.get('Choice_Field')
        Votes = request.POST.get('Votes')
    records = Grading_Results(
        Question = Question,
        Choice_Field = Choice_Field,
        Votes = Votes
    )
    records.save()
    return HttpResponseRedirect(reverse('index'))