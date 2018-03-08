from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Grat, Goal
from .forms import GratForm, GoalForm

# GRATITUDE

def indexGrat(request):
    # grat_list = Grat.objects.order_by('id')
    # form_grat = GratForm()
    # context = {'grat_list' : grat_list, 'form_grat' : form_grat}
    # return render(request, 'kofuku/index.html', context)

    grat_list = Grat.objects.order_by('id')
    form_grat = GratForm()  

    goal_list = Goal.objects.order_by('id')
    form_goal = GoalForm()

    context = {'grat_list' : grat_list, 'form_grat' : form_grat, 'goal_list' : goal_list, 'form_goal' : form_goal}
    return render(request, 'kofuku/index.html', context)

@require_POST
def addGrat(request):

    form_grat = GratForm(request.POST)
    if form_grat.is_valid():
        new_grat = Grat(text_grat=request.POST['text_grat'])
        new_grat.save()
    return redirect('indexgrat')

    

def completeGrat(request, grat_id):
    grat = Grat.objects.get(pk=grat_id)
    grat.complete_grat = True
    grat.save()

    return redirect('indexgrat')

#GOALS

def indexGoal(request):
    goal_list = Goal.objects.order_by('id')
    form_goal = GoalForm()
    context = {'goal_list' : goal_list, 'form_goal' : form_goal}
    return render(request, 'kofuku/index.html', context)

@require_POST
def addGoal(request):
    form_goal = GoalForm(request.POST)
    if form_goal.is_valid():
        new_goal = Goal(text_goal=request.POST['text_goal'])
        new_goal.save()
    return redirect('indexgrat')

def completeGoal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    goal.complete_goal = True
    goal.save()

    return redirect('indexgrat')
