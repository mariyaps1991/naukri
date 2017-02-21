from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, ApplicationForm
from .forms import JobApplication, CreateJob
from django.contrib.auth.models import User
from django.http import HttpResponse


def job_list(request):
    jobs = Job.objects.all().order_by('published_date')
    return render(request, 'job/job_list.html', {'jobs': jobs})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    job.application_count = ApplicationForm.objects.filter(title_id=pk).count()
    if request.user.is_anonymous:
        job.user_name = 'anonymous'
        job.save()
        return render(request, 'job/job_detail.html', {'job': job})
    else:
        me = User.objects.get(username=request.user)
        job.user_application_count = ApplicationForm.objects.filter(user_id=me.id).filter(title_id=pk).count()
    return render(request, 'job/job_detail.html', {'job': job})


def apply_job(request, pk):
    if request.method == 'POST':
        # form = JobApplication(request.POST, pk=pk)
        form = JobApplication(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.title = Job.objects.get(pk=pk)
            job.save()
            return redirect('job_list')
            # return HttpResponse("Job Applocation Form")
    else:
        form = JobApplication()
        # return HttpResponse("None POST. Job Applocation Form")
    return render(request, 'job/apply_job.html', {'form': form})


def register_naukri(request, pk):
    return render(request, 'job/registration.html')


def admin_dashboard(request):
    jobs = Job.objects.all()
    for job in jobs:
        job.application_count = ApplicationForm.objects.filter(title_id=job.id).count()
    job.save()
    return render(request, 'job/admin_dashboard.html', {'jobs':jobs})


def create_job(request):
    if request.method == 'POST':
        form = CreateJob(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('job_detail', pk=post.pk)
    else:
        form = CreateJob()

    return render(request, 'job/create_job.html', {'form': form})


def delete_job(request, pk):
    Job.objects.delete(id=pk)
    return redirect('/')
