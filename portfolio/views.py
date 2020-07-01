from django.shortcuts import render
from .models import Skill


# Create your views here.
def index(request):
    context = {
        "skills": Skill.objects.all()
    }
    return render(request, 'portfolio/index.html', context)
