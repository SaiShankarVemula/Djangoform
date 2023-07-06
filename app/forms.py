from django import forms


g=[('male','MALE'),('female','FEMALE')]

class Signupform(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g)
    