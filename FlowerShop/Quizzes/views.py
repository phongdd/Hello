from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice


# Create your views here.
def index(request):
	taisan = {"Điện Thoại", "Máy  tính", "Nhà", "Xe hơi"}
	context = {'name': "Đình Phong", "taisan": taisan}

	return render(request, "Quizzes/index.html", context)

def viewQuestion(request):
	questionList = Question.objects.all()
	questionContext = {'questionList': questionList}

	return render(request, "Quizzes/question.html", questionContext)

def viewChoice(request):
	choiceList = Choice.objects.all();
	choiceContext = { 'choiceList': choiceList }

	return render(request, "Quizzes/choice.html", choiceContext)

def detailView(request, question_id):
	question = Question.objects.get(pk = question_id)
	questionContext = {"question": question}
	
	return render(request, "Quizzes/detail_question.html", questionContext)

def vote(request, question_id):
	question = Question.objects.get(pk = question_id)	
	try:
		dulieu = request.POST["choice"]
		c = question.choice_set.get(pk = dulieu)
	except Exception:
		HttpResponse("Khong co du lieu!!!")
	c.vote += 1
	c.save()
	return render(request, "Quizzes/result.html", {"question": question})
	
	