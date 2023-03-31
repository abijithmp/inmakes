from . models import TaskName
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=TaskName
        fields=['name','priority','date']

