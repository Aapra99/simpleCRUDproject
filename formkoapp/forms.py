from django.forms import ModelForm
from .models import FormData


class AddForm(ModelForm):
    class Meta:
        model=FormData
        fields=['name','age','sex']

class FetchForm(ModelForm):
    class Meta:
        model=FormData
        fields=['name']