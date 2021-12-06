from django import forms
from myapp.models import *
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
    def clean(self):
        super(LoginForm,self).clean()
        userid=self.cleaned_data.get('userid')
        passwd=self.cleaned_data.get('passwd')
        
        if len(userid)<10:
            self._errors['userid']=self.error_class(
            ['User Name must be more than 10 Character'])
        if len(passwd)<8:
            self._errors['passwd']=self.error_class(
            ['Password can not be less than 8 char'])
        return self.cleaned_data