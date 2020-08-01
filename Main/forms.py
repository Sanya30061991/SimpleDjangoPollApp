from django.forms import ModelForm, TextInput, Textarea
from .models import Poll

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'option1', 'option2', 'option3']
        widgets = {
            'title': Textarea( attrs= {
                'class':"form-control",
                'placeholder':"Title of Poll"
            }),
            'option1': TextInput(attrs={
                'type':"text",
                'class':"form-control",
                'id':"option1",
                'placeholder':"Option 1"
            }),
            'option2': TextInput(attrs={
                'type':"text",
                'class':"form-control",
                'id':"option2",
                'placeholder':"Option 2"
            }),
            'option3': TextInput(attrs={
                'type':"text",
                'class':"form-control",
                'id':"option3",
                'placeholder':"Option 3"
            }),
        }