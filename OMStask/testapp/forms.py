from django import forms
from testapp.models import student
from django.contrib.auth.models import User


from passlib.hash import pbkdf2_sha256

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','mobile_number','email','userID']


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name', 'last_name']



