from django.forms import ModelForm
from .models import Filial, Region, Cekh

class FilialForm(ModelForm):
    class Meta:
        model = Filial
        fields = ['name', 'external_id']

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['name', 'filial']

class CekhForm(ModelForm):
    class Meta:
        model = Cekh
        fields = ['name','region']