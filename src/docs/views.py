from django.shortcuts import render
from .models import Patient
from .forms import Pat

# Create your views here.

def home(request):
	return render(request,'home.html',{})

def report(request):
	form = Pat(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context= {
	"form":form,
	
	}
	return render(request,"report.html",context)
