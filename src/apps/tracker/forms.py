from django.forms import ModelForm
from django import forms
from .models import FoodHistory

CHOICES=[('upcycled','Upcycle'),
         ('thrown_away','Throw it away')]

class FoodHistoryForm(forms.ModelForm):
    eaten = forms.ChoiceField(label= '', choices=CHOICES, widget=forms.RadioSelect())
    
    class Meta:
        model = FoodHistory
        fields = '__all__'
        #def __init__(self, *args, **kwargs):
        #    super(FoodHistoryForm, self).__init__(*args, **kwargs)
        #    # Hide specific fields using CSS
        #    self.fields['food'].widget.attrs['readonly'] = True
        #    self.fields['food'].widget.attrs['style'] = 'display: none;'
