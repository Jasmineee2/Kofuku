from django import forms

class GratForm(forms.Form):
    text_grat = forms.CharField(max_length=80,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder' : 'Enter your gratitude e.g. I am healthy!', 'aria-label' : 'Grat', 'aria-describedby' : 'add-btn-grat'}
        ))


class GoalForm(forms.Form):
    text_goal = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder' : 'Enter your goal e.g. complete XXX project', 'aria-label' : 'Goal', 'aria-describedby' : 'add-btn-goal'}
        ))
