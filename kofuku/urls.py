from django.urls import path
from . import views

urlpatterns = [
    #path('', views.indexGoal, name = 'indexgoal'),
    path('addgoal', views.addGoal, name='addgoal'),
    path('complete-goal/<goal_id>', views.completeGoal, name = 'completegoal'),  
    
    path('', views.indexGrat, name = 'indexgrat'),
    path('addgrat', views.addGrat, name='addgrat'),
    path('complete-grat/<grat_id>', views.completeGrat, name = 'completegrat'),


     

]