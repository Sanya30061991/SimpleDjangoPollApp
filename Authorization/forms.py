from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'password', 'last_name']
        widgets = {
            'first_name' : TextInput(attrs = {
                'type':"text",
                'class':"form-control",
                'placeholder':"Name"
            }),
            'email' : TextInput(attrs = {
                'type':"email",
                'class':"form-control",
                'placeholder':"Email Address"
            }),
            'password' : TextInput(attrs = {
                'type':"password",
                'class':"form-control",
                'placeholder':"Password"
            }),
            'last_name' : TextInput(attrs = {
                'type':"password",
                'class':"form-control",
                'placeholder':"Confirm Password"
            })
        }
