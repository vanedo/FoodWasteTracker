from django.forms import ModelForm
from django import forms
from .models import FoodHistory

CHOICES=[('upcycled','Upcycle'),
         ('thrown_away','Throw it away')]

class FoodHistoryForm(forms.ModelForm):
    eaten = forms.ChoiceField(label= 'Action', choices=CHOICES, widget=forms.RadioSelect())
    
    class Meta:
        model = FoodHistory
        #exclude = ('food',)
        readonly_fields=('food', )

        fields = '__all__'

