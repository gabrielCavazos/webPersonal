from django.shortcuts import render
from .models import Skills, Experience, Education, Projects
# Create your views here.


def home(request):
    skills = Skills.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()

    projects = Projects.objects.all()
    context = {"skills": skills, "experiences": experience,
               "educations": education, "projects": projects}
    return render(request, "core/index.html", context)


def contact(request):
    return render(request, "core/contact.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def blog(request):
    return render(request, "core/blog.html")


def services(request):
    return render(request, "core/services.html")
