from django import forms
from .models import *

class general_form(forms.ModelForm):
    class Meta:
        model=general_identification_and_parentage
        fields='__all__'

class disposal_form(forms.ModelForm):
    class Meta:
        model=disposal_culling
        fields='__all__'

class nutrition_form(forms.ModelForm):
    class Meta:
        model=nutrition_and_feeding
        fields='__all__'

class economics_form(forms.ModelForm):
    class Meta:
        model=economics
        fields='__all__'

class efficiency_form(forms.ModelForm):
    class Meta:
        model=efficiency_parameter
        fields='__all__'

class qualification_form(forms.ModelForm):
    class Meta:
        model=qualification_boar
        fields='__all__'

class service_form(forms.ModelForm):
    class Meta:
        model=service_record
        fields='__all__'

