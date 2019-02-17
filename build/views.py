from django.views.generic import TemplateView
from build.models import PageCounter, Team
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
		return context

class TeamListView(ListView):
	model = Team
	template_name = 'build/team_list.html'