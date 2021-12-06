from django import forms
from myapp.models import *
class ImageForm(forms.ModelForm):
    fname=forms.CharField(label='First Name',max_length=50)
    email=forms.EmailField(label='Email Address')
    file=forms.FileField()
    
    class Meta:
        model=MyImage
        fields='__all__'