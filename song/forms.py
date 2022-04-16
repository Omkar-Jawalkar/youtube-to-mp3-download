

from dataclasses import field
from django.forms import ModelForm

from song.models import songmodel


class songForm(ModelForm):
    class Meta:
        model = songmodel
        fields = ['songname', 'songurl']
   