from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class StudentForm(forms.Form):
    roll_no=forms.IntegerField(help_text='your roll number.')
    name=forms.CharField(help_text='your name must be starts with s.')

    def clean_name(self):
        data=self.cleaned_data['name']
        if data.lower()[0] != 's':
            raise ValidationError(_("your name must start with 's'"))
        return data