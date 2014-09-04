from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from . import models, utils

def home(request):
    return render(request, 'home.html',
                  {'profiles': models.Profile.objects.all()})

def profile(request, pk):
    return render(request, 'profile.html',
        {'profile': get_object_or_404(models.Profile, pk=pk)})

def company(request, pk):
    return render(request, 'company.html',
        {'company': get_object_or_404(models.Company, pk=pk)})

def job_title(request, pk):
    return render(request, 'job_title.html',
        {'job_title': get_object_or_404(models.JobTitle, pk=pk)})

@login_required
@require_POST
def create_profile(request):
    profile = utils.fake_profile()
    return render(request, 'profile.html',
        {'profile': profile})

def probe(request):
    models.Profile.objects.filter(id=1).exists()
    return HttpResponse('success')
