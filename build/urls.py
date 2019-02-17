from django.urls import path

from . import views

app_name = 'build'

urlpatterns = [
	path('home', views.HomeView.as_view(), name='home'),
    path('team-list', views.TeamListView.as_view(), name='team_list'),
    path('team-detail/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
    path('team-add', views.TeamCreateView.as_view(), name='team_add'),
    path('team-edit/<int:pk>/', views.TeamUpdateView.as_view(), name='team_edit'),
]