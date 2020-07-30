from django.forms import ModelForm, TextInput, Textarea
from .models import Poll

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'option1', 'option2', 'option3']