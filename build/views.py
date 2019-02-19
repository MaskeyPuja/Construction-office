from django.views.generic import TemplateView
from build.models import PageCounter, Team, Career
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TeamForm, CareerForm


class HomeView(TemplateView):

	template_name = 'build/index.html'
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if PageCounter.objects.first():
			total_count = PageCounter.objects.first()
			total_count.total_count += 1
			total_count.save()
		else:
			total_count = PageCounter()
			total_count.total_count = 1
			total_count.save()

		team = Team.objects.all()
		context['team'] = team

		return context

class AboutView(TemplateView):

	template_name = 'build/about-us.html'

class TeamListView(ListView):
	model = Team
	template_name = 'build/team_list.html'

class TeamDetailView(DetailView):
	model = Team
	template_name = 'build/team_detail.html'

class TeamCreateView(CreateView):
	model = Team
	template_name = 'build/team_form.html'
	form_class = TeamForm
	success_url = reverse_lazy('build:team_list')

class TeamUpdateView(UpdateView):
	model = Team
	template_name = 'build/team_form.html'
	form_class = TeamForm
	success_url = reverse_lazy('build:team_list')

class TeamDeleteView(DeleteView):
	model = Team
	template_name = 'build/team_delete.html'
	success_url = reverse_lazy('build:team_list')


class CareerListView(ListView):
	model = Career
	template_name = 'build/career_list.html'

class CareerDetailView(DetailView):
	model = Career
	template_name = 'build/career_detail.html'

class CareerCreateView(CreateView):
	model = Career
	template_name = 'build/career_form.html'
	form_class = CareerForm
	success_url = reverse_lazy('build:career_list')

class CareerUpdateView(UpdateView):
	model = Career
	template_name = 'build/career_form.html'
	form_class = CareerForm
	success_url = reverse_lazy('build:career_list')

class CareerDeleteView(DeleteView):
	model = Career
	template_name = 'build/career_delete.html'
	success_url = reverse_lazy('build:career_list')


