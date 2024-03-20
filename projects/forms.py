
from django import forms
from django.core.validators import EmailValidator
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout

class ContactForm(forms.Form):
    #name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;'}))
    #email = forms.CharField(validators=[EmailValidator()], widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;'}))
    #message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'style': 'width: 900px;', 'class': 'form-control'}))
    

#from django import forms
#from django.core.validators import EmailValidator


#class ContactForm(forms.Form):
    #name = forms.CharField(max_length=100)
    #email = forms.CharField(validators=[EmailValidator()])
    #phone = forms.CharField(max_length=15)
    #subject = forms.CharField(max_length=100)
    #message = forms.CharField(widget=forms.Textarea)    