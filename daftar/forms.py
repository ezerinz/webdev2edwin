from django import forms
from .models import Pendaftaran


class PendaftaranForm(forms.ModelForm):
    class Meta:
        model = Pendaftaran
        fields = ["nama", "alamat", "no_telp"]
        widgets = {
            "nama": forms.TextInput(attrs={"class": "form-control"}),
            "alamat": forms.TextInput(attrs={"class": "form-control"}),
            "no_telp": forms.TextInput(attrs={"class": "form-control"}),
        }
