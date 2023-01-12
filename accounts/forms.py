from tkinter import Label
from django import forms

class Loginform(forms.Form):
    username= forms.CharField(label="Kullaıcı Adı ")
    password=forms.CharField(label="Parola",widget=forms.PasswordInput)

class Registerform(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=50,label="Parola",widget=forms.PasswordInput)
    confirm =forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)

