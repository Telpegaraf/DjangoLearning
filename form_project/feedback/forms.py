from django import forms
from .models import Feedback


#class FeedbackForm(forms.Form):
#    name = forms.CharField(label='Имя', max_length=8, min_length=4)
#    surname = forms.CharField(label='Фамилия', max_length=8, min_length=4)
#    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols':40}))
#    rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name': {'max_length': 'ой как много символов',
                     'min_length': 'ой как мало символов',
                     'required': 'Не должно быть пустым'
                     },
            'surname': {'max_length': 'ой как много символов',
                        'min_length': 'ой как мало символов',
                        'required': 'Не должно быть пустым'
                        },
            'feedback': {'max_length': 'ой как много символов',
                         'min_length': 'ой как мало символов',
                         'required': 'Не должно быть пустым'
                         }
        }