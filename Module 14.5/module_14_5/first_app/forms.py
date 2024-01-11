from django import forms
from django.core import validators

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class contactForm(forms.Form):
        name = forms.CharField(label="Full Name",required = False,max_length = 20,validators=[validators.MinLengthValidator(10,message='Enter a name with at least 10 characters')])
        email = forms.EmailField(label="Email address")
        age = forms.IntegerField()
        birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
        birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
        agree = forms.BooleanField(initial=True)
        favorite_color = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES)
        favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)