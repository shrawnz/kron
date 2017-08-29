from django.conf.urls import url

from . import views

app_name = 'kronFrame'
urlpatterns = [
	url(r'^inDev/', views.IndexView.as_view(), name='index'),
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^populate/', views.PopulateView.as_view(), name='populate'),
	url(r'^offered/', views.OfferedView.as_view(), name='offered'),
]