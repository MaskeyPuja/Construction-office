from django import forms
from .models import Team

class TeamForm(forms.ModelForm):

	class Meta:
		model = Team
		fields = ('full_name', 'position', 'image')