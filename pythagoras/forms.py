from django import forms
from nhansohoc import settings


class CandidateForm(forms.Form):
    last_name = forms.CharField(label="Họ", max_length=200)
    first_name = forms.CharField(label="Tên", max_length=200)
    date_of_birth = forms.DateField(
        label="Ngày Sinh",
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker', 'type': 'date'})
    )