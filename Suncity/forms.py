from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Program, CustomUser

class Signup_Form(UserCreationForm):
    email = forms.EmailField(max_length=100, required= True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
    



class Signin_Form(forms.Form):
    Email = forms.EmailField(required=True, widget=forms.EmailInput)
    Password = forms.CharField(required=True, widget=forms.PasswordInput)


class Search_Form(forms.Form):
    search = forms.CharField(min_length=2)
    search_in = forms.ChoiceField(label= [Program.name, Program.Date])


class Program_Form(forms.ModelForm):
    class Meta:
        model = Program
        fields = ("__all__")
        

        


