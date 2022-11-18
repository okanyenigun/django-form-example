from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


from django import forms

class AnyForm(forms.Form):

    model_name = forms.CharField(label="Model Name",max_length=100, 
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': ('Model Name')
                                    }))
    brand = forms.CharField(label="Brand", max_length=100,
                            widget=forms.TextInput(
                                    attrs={
                                        'placeholder': ('Brand')
                                    }))
    price = forms.IntegerField(label="Price")
    status_choices = [('new', 'New'), ('used','Used')]
    status = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=status_choices)

class PlayerForm(forms.Form):

    name = forms.CharField(max_length=100)
    team = forms.CharField(max_length=100)