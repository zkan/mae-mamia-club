import datetime

from django import forms

from .models import Member
from .utils import get_days, get_months, get_years


class MemberForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=300,
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
        required=True
    )

    mom_name = forms.CharField(
        label='Mom Name',
        max_length=300,
        required=True
    )

    def save(self):
        data = self.cleaned_data

        day = int(data['birth_day'])
        month = int(data['birth_month'])
        year = int(data['birth_year'])

        member = Member()
        member.name = data['name']
        member.birthdate = datetime.date(year, month, day)
        member.dad_name = data['dad_name']
        member.mom_name = data['mom_name']
        member.save()

        return member.id
