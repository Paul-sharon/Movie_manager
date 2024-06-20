from django.forms import ModelForm
from . models import MovieInfo
class MovieForm(ModelForm):  #ModelForm is inherited to MovieForm#
    class Meta: #used to describe main class property#
        model=MovieInfo
        fields='__all__'
