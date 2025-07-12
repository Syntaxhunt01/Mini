from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task..'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-contrl'}),
            'priority': forms.Select(attrs={'class': 'form-control'})
        }