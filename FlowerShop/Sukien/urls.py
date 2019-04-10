from django.urls import path
from . import views

app_name = "sukien"
urlpatterns = [
	#path('', views.home, name='sukien_home'),
	path('add/', views.add_post, name='add'),
	path('save/', views.save_post, name='save'),
	
	path('email/', views.email_view, name='email'),
	path('goi/', views.process, name='process'),

	path('', views.IndexClass.as_view(), name='sukien_home'),
]