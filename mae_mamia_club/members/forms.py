from django import forms


class MemberForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name'
            }
        )
    )

    birth_day = forms.ChoiceField(
        label='Birth Day',
        choices=(('', ''), ('1', '01'), ('2', '02'))
    )

    birth_month = forms.ChoiceField(
        label='Birth Month',
        choices=(('', ''), ('1', '01'), ('2', '02'))
    )

    birth_year = forms.ChoiceField(
        label='Birth Year',
        choices=(('', ''), ('2010', '2010'), ('2011', '2012'))
    )

    dad_name = forms.CharField(
        label='Dad Name',
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Dad Name'
            }
        )
    )

    mom_name = forms.CharField(
        label='Mom Name',
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Mom Name'
            }
        )
    )
