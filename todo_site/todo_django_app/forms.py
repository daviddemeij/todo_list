from django import forms

class todoForm(forms.Form):
    todo = forms.CharField(label='Add Todo', max_length=100)
