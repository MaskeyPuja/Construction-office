from django import forms
from .models import Team, Career

class TeamForm(forms.ModelForm):

	class Meta:
		model = Team
		fields = ('full_name', 'position', 'image')

class CareerForm(forms.ModelForm):

	class Meta:
		model = Career
		fields = ('title', 'pub_date', 'due_date', 'job_des', 'qualification')