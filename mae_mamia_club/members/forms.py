from django import forms

from .utils import get_days, get_months, get_years


class MemberForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name'
            }
        ),
        required=True
    )

    birth_day = forms.ChoiceField(
        label='Birth Day',
        choices=get_days(),
        required=True
    )

    birth_month = forms.ChoiceField(
        label='Birth Month',
        choices=get_months(),
        required=True
    )

    birth_year = forms.ChoiceField(
        label='Birth Year',
        choices=get_years(),
        required=True
    )

    dad_name = forms.CharField(
        label='Dad Name',
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Dad Name'
            }
        ),
        required=True
    )

    mom_name = forms.CharField(
        label='Mom Name',
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Mom Name'
            }
        ),
        required=True
    )
