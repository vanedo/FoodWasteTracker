from django.forms import ModelForm, ModelChoiceField
from django import forms
from .models import FoodHistory, FoodAdvice

CHOICES=[('upcycled','Upcycle it'),
         ('thrown_away','Throw it away')]

class FoodHistoryForm(forms.ModelForm):
    eaten = forms.ChoiceField(label= '', choices=CHOICES, widget=forms.RadioSelect())
    
    class Meta:
        model = FoodHistory
        fields = '__all__'
        widgets = {
            'food':forms.Select(attrs={'disabled':'true'})
        }
        #def __init__(self, *args, **kwargs):
        #    super(FoodHistoryForm, self).__init__(*args, **kwargs)
        #    # Hide specific fields using CSS
        #    self.fields['food'].widget.attrs['readonly'] = True
        #    self.fields['food'].widget.attrs['style'] = 'display: none;'

class FoodChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.getFoodDetails()

class ContributeDataForm(forms.ModelForm):
    #food = FoodChoiceField(queryset=FoodHistory.objects.all())
    class Meta:
        model = FoodHistory
        fields = ('food', 'eaten')
        widgets = {
            'food': forms.Select(attrs={'class':'form-control'}),
            'eaten': forms.Select(attrs={'class':'form-control', 
                                         "data-tooltip":"text info", "data-tooltip-location":"top"})
         }
        labels = {
            'food':'Select food',
            'eaten':'What will you do with this item?'
        }
