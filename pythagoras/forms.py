from django import forms


class CandidateForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=200)
    last_name = forms.CharField(label="Last Name", max_length=200)
    date_of_birth = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    )
