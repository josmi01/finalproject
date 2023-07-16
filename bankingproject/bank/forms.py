from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
# class LoginForm(AuthenticationForm):
#     username = forms.Username_Field(max_length=254, help_text='Required. Inform a valid eusername.')
#     class Meta:
#         model = User
#         fields = ('username','password',)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
class AccountForm(forms.Form):
    name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    age = forms.IntegerField()
    email = forms.EmailField(max_length=50)
    address = forms.CharField(max_length=100)
    district = forms.CharField(max_length=30)
    branch = forms.CharField(max_length=20)
    account_type = forms.CharField(max_length=20)
    materials = forms.CharField()

    class Meta:
        model = User
        fields=('name','date_of_birth','age','email','address','district','branch','account_type','materials')