from . models import table
from django import forms
class tabform(forms.ModelForm):
    class Meta:
        model=table
        fields=['name','priority','date']