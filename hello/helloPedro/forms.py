# -*- coding: utf-8 -*-
from django import forms

class NameGetter(forms.Form):
    greeting = forms.CharField(label='Saludo', max_length=25)
    name = forms.CharField(label='Nombre', max_length=25)
