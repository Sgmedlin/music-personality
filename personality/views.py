from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# from .models import Choice, Question, Suggestion
from django.utils import timezone
from django.views.generic import CreateView

def home(request):
	return render(request, 'home.html')


# class HomeView(CreateView):
#     template_name = 'personality/home.html'
    # context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """
    #     Return the last five published questions (not including those set to be
    #     published in the future).
    #     """
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]
# Create your views here.
