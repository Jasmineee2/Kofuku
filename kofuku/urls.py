from django.urls import path
from . import views

urlpatterns = [
    #path('', views.indexGoal, name = 'indexgoal'),

    path('', views.index, name = 'index'),
    path('history', views.history, name = 'history'),

    path('addgrat', views.addGrat, name='addgrat'),
    path('complete-grat/<grat_id>', views.completeGrat, name = 'completegrat'),
    path('delete-grat/<grat_id>', views.deleteGrat, name="deletegrat"),
    path('deletegratcomplete', views.deleteGratCompleted, name="deletegratcomplete"),
    path('deletegratall', views.deleteGratAll, name='deletegratall'),
    path('saveGrat', views.saveGrat, name='savegrat'),


    path('addgoal', views.addGoal, name='addgoal'),
    path('complete-goal/<goal_id>', views.completeGoal, name = 'completegoal'),
    path('delete-goal/<goal_id>', views.deleteGoal, name="deletegoal"),
    path('deletegoalcomplete', views.deleteGoalCompleted, name="deletegoalcomplete"),
    path('deletegoalall', views.deleteGoalAll, name='deletegoalall'),

    
   
]


     

