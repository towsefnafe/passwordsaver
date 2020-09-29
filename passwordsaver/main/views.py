from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewList
from .models import passsave

def home(response):
    return render(response, "main/home.html", {})

def detail(response, id):
	ls = passsave.objects.get(id=id)
	
	if ls in response.user.passsave.all():
		ls = passsave.objects.get(id=id)
		return render(response, "main/detail.html", {"ls":ls})
	return render(response, "main/home.html", {})

def add(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			website = form.cleaned_data["website"]
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			t = passsave(website=website, username=username, password=password)
			t.save()
			response.user.passsave.add(t)

			return HttpResponseRedirect("/%i" %t.id)

	else:
		form = CreateNewList()

	return render(response, "main/add.html", {"form":form})

def view(response):
	ls = passsave.objects.all()
	return render(response, "main/view.html", {"ls":ls})