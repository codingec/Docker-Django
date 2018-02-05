# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

class NameGetter(forms.Form):
    greeting = forms.CharField(label='Saludo', max_length=25)
    name = forms.CharField(label='Nombre', widget=forms.PasswordInput)
