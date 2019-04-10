from django.urls import path
from . import views

app_name = 'quizzes'
urlpatterns = [
	path('', views.index, name='quizzes_index'),
	path('question/', views.viewQuestion, name = 'quizzes_viewQuestion'),
	path('choice/', views.viewChoice, name = 'quizzes_viewChoice'),
	path('detail/<int:question_id>/', views.detailView, name = 'quizzes_detailView'),
	path('<int:question_id>/', views.vote, name = 'quizzes_vote'),
	
] 