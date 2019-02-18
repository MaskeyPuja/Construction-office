from django.urls import path

from . import views

app_name = 'build'

urlpatterns = [
    path('team-list', views.TeamListView.as_view(), name='team_list'),
    path('team-detail/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
    path('team-add', views.TeamCreateView.as_view(), name='team_add'),
    path('team-edit/<int:pk>/', views.TeamUpdateView.as_view(), name='team_edit'),
    path('team-delete/<int:pk>/', views.TeamDeleteView.as_view(), name='team_delete'),

    path('career-list', views.CareerListView.as_view(), name='career_list'),
    path('career-detail/<int:pk>/', views.CareerDetailView.as_view(), name='career_detail'),
]