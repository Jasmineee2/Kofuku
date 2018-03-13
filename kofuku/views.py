from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Grat, Goal
from .forms import GratForm, GoalForm
from datetime import datetime

# GRATITUDE

def index(request):
    # grat_list = Grat.objects.order_by('id')
    # form_grat = GratForm()
    # context = {'grat_list' : grat_list, 'form_grat' : form_grat}
    # return render(request, 'kofuku/index.html', context)

    grat_list = Grat.objects.filter(save_grat=False).order_by('id')
    #grat_list = [ grat for grat in grat_aux if grat.save_grat == False ]
    form_grat = GratForm()  

    goal_list = Goal.objects.order_by('id')
    form_goal = GoalForm()

    context = {'grat_list' : grat_list, 'form_grat' : form_grat, 'goal_list' : goal_list, 'form_goal' : form_goal}
    return render(request, 'kofuku/index.html', context)

def history(request):
    grat_list = Grat.objects.order_by('id')
    form_grat = GratForm()  

    goal_list = Goal.objects.order_by('id')
    form_goal = GoalForm()

    context = {'grat_list' : grat_list, 'form_grat' : form_grat, 'goal_list' : goal_list, 'form_goal' : form_goal}
    
    return render(request, 'kofuku/history.html', context)

@require_POST
def addGrat(request):

    form_grat = GratForm(request.POST)
    if form_grat.is_valid():
        new_grat = Grat(text_grat=request.POST['text_grat'])
        new_grat.save()
    return redirect('index')

    

def completeGrat(request, grat_id):
    grat = Grat.objects.get(pk=grat_id)
    grat.complete_grat = True
    grat.save()

    return redirect('index')

def deleteGrat(request, grat_id):
    grat = Grat.objects.get(pk=grat_id)
    grat.delete_grat = True
    grat.delete()
    return redirect('index')

def deleteGratCompleted(request):
    Grat.objects.filter(complete_grat__exact=True).delete()
    return redirect('index')
    
def deleteGratAll(request):
    Grat.objects.all().delete()
    return redirect('index')

def saveGrat(request):
    grats = Grat.objects.filter(save_grat=False)
    for grat in grats:
        grat.save_grat = True
        grat.save()

    return redirect('index')

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
    return redirect('index')

def completeGoal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    goal.complete_goal = True
    goal.save()

    return redirect('index')

def deleteGoal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    goal.delete_goal = True
    goal.delete()
    return redirect('index')

def deleteGoalCompleted(request):
    Goal.objects.filter(complete_goal__exact=True).delete()
    return redirect('index')
    
def deleteGoalAll(request):
    Goal.objects.all().delete()
    return redirect('index')
