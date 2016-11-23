# coding=utf-8

from django import forms
from quarry.models import TruckModel


class TruckModelFilter(forms.Form):
    model = forms.ModelChoiceField(
        label='Модель',
        empty_label='Все',
        queryset=TruckModel.objects.all(),
        required=False
    )

    def execute(self, queryset):
        model = self.cleaned_data.get('model')
        if model:
            queryset = queryset.filter(model=model)

        return queryset
