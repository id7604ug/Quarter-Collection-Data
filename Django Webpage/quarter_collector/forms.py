from django import forms
from .models import Quarter

class QuarterForm(forms.ModelForm):
    class Meta:
        model = Quarter
        fields = ('state_code', 'state', 'year_issued', 'description', 'owned')
