from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
# Create your views here.
from django.views import View

def home(request):
	return HttpResponse("Sự Kiện")

def add_post(request):
	a = PostForm()
	return render(request, 'Sukien/add_Sukien.html', {'f': a})

def save_post(request):	
	if  request.method == "POST":
		q = PostForm(request.POST)
		if q.is_valid():
			q.save()
			return HttpResponse("Luu OK")
		else:
			return HttpResponse("Du lieu ko hop le!")
	else:
		return HttpResponse("Khong phai Post request")

def email_view(request):
	b = SendEmail()
	return render(request, 'Sukien/email.html', {'f': b})

def process(request):
	if request.method == "POST":
		e = SendEmail(request.POST)
		if e.is_valid():
			# tieude = e.cleaned_data['title']
			# noidung = e.cleaned_data['content']
			# cc = e.cleaned_data['cc']
			# email = e.cleaned_data['email']
			# context = { 'tieude': tieude, 'noidung': noidung, 'cc': cc, 'email':email}
			#return render(request, 'Sukien/print_email.html', context)

			context2 = {'email_data': e}			
			return render(request, 'Sukien/print_email.html', context2)
		else:
			return HttpResponse("Form not valid")
	else:
		return HttpResponse("NOT POST")

class IndexClass(View):
	def get(self, request):
		return HttpResponse("Sự Kiện")


	