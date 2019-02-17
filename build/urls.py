from django.urls import path

from . import views

app_name = 'build'

urlpatterns = [
	# path('home', HomeView.as_view(), name='home'),
    path('team-list', views.TeamListView.as_view(), name='team_list'),
]