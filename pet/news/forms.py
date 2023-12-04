from .models import Artikles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtiklesForm(ModelForm):
    class Meta:
        model = Artikles
        fields = ['title', 'anons', 'content', 'date']
        
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
                
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержимое статьи'
            })
        }