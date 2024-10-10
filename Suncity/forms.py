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




class Program_Form(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name','Location','Date','Dress_code','Description','start_time','cover_photo')


class Search_Form(forms.Form):
    query = forms.CharField(max_length=250, label = 'search')
        

        


