import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Member
from .utils import get_days, get_months, get_years

from django.contrib.admin.widgets import AdminDateWidget

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

#credit http://chriskief.com/2013/10/19/limiting-upload-file-size-with-django-forms/
class RestrictedImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        self.max_upload_size = kwargs.pop('max_upload_size', None)
        super(RestrictedImageField, self).__init__(*args, **kwargs)
 
    def clean(self, *args, **kwargs):
        data = super(RestrictedImageField, self).clean(*args, **kwargs)
        try:
            if data.size > self.max_upload_size:
                self.error_messages = { 'file_size':_('File size must be under %s. Current file size is %s.') % (filesizeformat(self.max_upload_size), filesizeformat(data.size))}
                
                raise forms.ValidationError(
                        self.error_messages['file_size'],
                        code='file_size',)
                
        except AttributeError:
            pass
 
        return data

class MemberForm(forms.ModelForm):
    birthdate = forms.DateField(widget = SelectDateWidget(years=(2013, 2014)))
    image = RestrictedImageField(max_upload_size=1048576)
    gender = forms.ChoiceField(
        label='Gender',
        choices=(('','-----------'),('g', 'girl'),('b', 'boy') ),
        required=True,
    )

    class Meta:
        model = Member

class MemberGenerateImageForm(forms.Form):

    image = RestrictedImageField(max_upload_size=1048576)

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
