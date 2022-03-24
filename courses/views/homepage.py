from django.shortcuts import HttpResponse
from django.shortcuts import render
from courses.models import Course


def home(request):
    courses = Course.objects.all()

    return render(request, "courses/index.html", context={'courses':courses})