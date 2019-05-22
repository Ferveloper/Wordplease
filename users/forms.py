from django import forms


class LoginForm(forms.Form):

    usr = forms.CharField(label='Usuario')
    pwd = forms.CharField(label='Contraseña', widget=forms.PasswordInput())


class SignupForm(forms.Form):

    fname = forms.CharField(label='Nombre')
    lname = forms.CharField(label='Apellidos')
    email = forms.EmailField(label='Email')
    usr = forms.CharField(label='Usuario')
    pwd = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
