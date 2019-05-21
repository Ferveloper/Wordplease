from django import forms


class LoginForm(forms.Form):

    usr = forms.CharField(label='Username')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput())


class SignupForm(forms.Form):

    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    usr = forms.CharField(label='Username')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput())
