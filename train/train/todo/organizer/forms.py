from .models import Task
from django import forms

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Task
        #fields = ['name', 'priority', 'date']
        fields = '__all__'