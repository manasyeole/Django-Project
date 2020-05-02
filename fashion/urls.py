from django.urls import path
from . import views

app_name="fashion"

urlpatterns = [
		path('index',views.index, name='index'),
		path('coronaupdates',views.coronaupdates, name='coronaupdates')

	]