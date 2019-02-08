from django import forms
from .models import Patient



class Pat(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['name','pid','symptoms','weight','prescriptions','report']


