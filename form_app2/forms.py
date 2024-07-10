from django import forms


class MessageForm(forms.Form):
    CHOICES = [
        ("", "---------"),
        ("question", "Pytanie"),
        ("other", "Inne")
    ]

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(label="Treść", widget=forms.Textarea)
    date = forms.DateField(label="Ulubiona data", widget=forms.widgets.NumberInput(attrs={'type': 'date'}))
    time = forms.TimeField(label="Ulubiony czas", widget=forms.widgets.NumberInput(attrs={'type': 'time'}))
