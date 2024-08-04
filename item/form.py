from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['city']
        
        
        widget ={
        'city': forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
    }
