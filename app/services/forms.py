from django import forms

from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-textColor focus:outline-none focus:ring-primary focus:border-primary'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-textColor focus:outline-none focus:ring-primary focus:border-primary',
                'rows': 3
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-textColor focus:outline-none focus:ring-primary focus:border-primary',
                'step': '0.01'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-textColor focus:outline-none focus:ring-primary focus:border-primary',
                'min': '1'
            })
        }