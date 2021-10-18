from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import New, Person, Partner, Service
from .forms import ContactForm
from django.core.mail import send_mail
from django.urls import reverse_lazy


class HomeView(generic.View):
	def get(self, request, *args, **kwargs):
		news = New.objects.filter(is_publish=True).all()[:3]
		partners = Partner.objects.all()
		team = Person.objects.all()
		services = Service.objects.all()
		form = ContactForm()
		return render(request, "index.html", {"services" : services, "form" : form, "news" : news, "partners" : partners, "team" : team})

	def post(self, request, *args, **kwargs):
		form = ContactForm(request.POST)
		news = New.objects.filter(is_publish=True).all()[:3]
		partners = Partner.objects.all()
		services = Service.objects.all()
		team = Person.objects.all()

		if form.is_valid():
			cd = form.cleaned_data
			subject = "Sent comment"
			message = f"Comment\n{cd['comment']}\n\nPhone: {cd['phone']}\nFrom: {cd['email']}"
			send_mail(
				subject,
				message,
				"zolotojznak@gmail.com",
				["zolotojznak@gmail.com"],
				fail_silently=False
			)
			form.save()
			return redirect(reverse_lazy('news:list'))
		
		return render(request, "index.html", {"services": services, "form": form, "news": news, "partners": partners, "team": team})
	

class AllNewsView(generic.View):

	def get(self, request, *args, **kwargs):
		news = New.objects.filter(is_publish=True).all()
		return render(request, "all-news.html", {"news" : news})


class NewsDetailView(generic.DetailView):
	template_name = "news_detail.html"

	def get(self, request, pk, *args, **kwargs):
		news = 	get_object_or_404(New, pk=pk)
		return render(request, self.template_name, {"news" : news})
