from django import forms
from.models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text', 'votes', 'question']