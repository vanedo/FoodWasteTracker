from django.forms import ModelForm
from django import forms
from .models import FoodHistory

CHOICES=[('upcycled','Upcycle'),
         ('thrown_away','Throw it away')]

class FoodHistoryForm(forms.ModelForm):
    eaten = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = FoodHistory
        #exclude = ('food',)
        fields = '__all__'
        labels = {
            'food': 'Food name',
            'eaten': 'Action',
        }
