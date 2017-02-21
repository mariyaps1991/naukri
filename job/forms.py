from django import forms
from .models import ApplicationForm, Job


class JobApplication(forms.ModelForm):

    class Meta:
        model = ApplicationForm
        file = forms.FileField()
        fields = ('first_name', 'last_name', 'notice_period')


# Fields
# title = models.CharField(max_length=200)
# company_name = models.CharField(max_length=100)
# description = models.TextField()
# created_by = models.ForeignKey('auth.user', on_delete=models.CASCADE)
# created_date = models.DateTimeField(default=timezone.now)
# published_date = models.DateTimeField(blank=True, null=True)
# job_status = models.CharField(max_length=9, choices=JOB_PUBLISHED_STATUS, default="PENDING")


class CreateJob(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('title', 'company_name', 'description')
