from django.views.generic import TemplateView

class HomeView(TemplateView):

	template_name = 'build/index.html'
	# print('hello')