from django import forms
from .models import *


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Note..."}),
            'title': forms.Textarea(attrs={'content': 'form-control', 'placeholder': "Write your note here..."})
        }