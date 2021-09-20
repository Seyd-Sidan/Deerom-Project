from django.urls import path
from .import views
urlpatterns = [
	path('',views.home,name='homepg'),
	path('playerpg',views.playerpg),
	path('playeradd',views.playeradd),
	path('display',views.display),
	path('remplr',views.remplr),
	path('remplayer',views.remplayer),

]