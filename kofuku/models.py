from django.db import models

class Grat(models.Model):
    text_grat = models.CharField(max_length=80)
    complete_grat = models.BooleanField(default=False)
    save_grat = models.BooleanField(default=False)

    def __str__(self):
        return self.text_grat

class Goal(models.Model):
    text_goal = models.CharField(max_length=40)
    complete_goal = models.BooleanField(default=False)

    def __str__(self):
        return self.text_goal
