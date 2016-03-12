from django import forms

from .models import Scrim


class ScrimForm(forms.ModelForm):
    class Meta:
        model = Scrim
        fields = ('team_name', 'team_captain', 'region')
