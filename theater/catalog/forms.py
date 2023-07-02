from django import forms
from .models import *


class AddPlayForm(forms.ModelForm):

    class Meta:
        model = Play
        fields = "__all__"
