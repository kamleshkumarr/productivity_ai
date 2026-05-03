from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',   # ✅ shows date-time picker
                'class': 'form-control'
            }
        ),
        input_formats=['%Y-%m-%dT%H:%M']  # ✅ important
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']