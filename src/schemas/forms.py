from django import forms
from django.forms import inlineformset_factory

from .models import Schema, Column


class SchemaForm(forms.ModelForm):
    """
    Form representing Schema model.
    """

    class Meta:
        model = Schema
        fields = ('name',)


class ColumnForm(forms.ModelForm):
    """
    Form representing Column model.
    """

    class Meta:
        model = Column
        fields = ('name', 'datatype', 'order',)


ColumnFormSet = inlineformset_factory(Schema, Column, form=ColumnForm, extra=1, can_delete=False)
ColumnUpdateFormSet = inlineformset_factory(Schema, Column, form=ColumnForm, extra=1)
