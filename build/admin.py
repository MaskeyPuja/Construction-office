from django.contrib import admin
from .models import PageCounter, Team, Career

# Register your models here.
admin.site.register(PageCounter)
admin.site.register(Team)
admin.site.register(Career)