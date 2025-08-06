from django import forms


class ReportForm(forms.Form):
    start_date = forms.DateField(label="Início", widget=forms.DateInput(attrs={"type": "date"}))
    end_date = forms.DateField(label="Fim", widget=forms.DateInput(attrs={"type": "date"}))
