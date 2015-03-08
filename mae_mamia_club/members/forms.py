import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Member
from .utils import get_days, get_months, get_years

from django.contrib.admin.widgets import AdminDateWidget


class MemberForm(forms.ModelForm):
    birthdate = forms.DateField(widget = SelectDateWidget(years=(2013, 2014)))

    class Meta:
        model = Member

class MemberGenerateImageForm(forms.Form):

    image = forms.ImageField()

    def save(self):
        data = self.cleaned_data

        day = int(data['birth_day'])
        month = int(data['birth_month'])
        year = int(data['birth_year'])

        member = Member()
        member.nickname = data['nickname']
        member.firstname = data['firstname']
        member.lastname = data['lastname']
        member.birthdate = datetime.date(year, month, day)
        member.dad_name = data['dad_name']
        member.mom_name = data['mom_name']
        member.address = data['address']
        member.province = data['province']
        member.gender = data['gender']
        member.image = data['image']
        member.save()

        return member.id
