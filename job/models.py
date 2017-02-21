from django.db import models
from django.utils import timezone


class Job(models.Model):

    # Choices
    JOB_PUBLISHED_STATUS = (
        ("PENDING", "Pending"),
        ("REVIEWED", "Reviewed"),
        ("PUBLISHED", "Published"),
    )

    # Fields
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    job_status = models.CharField(max_length=9, choices=JOB_PUBLISHED_STATUS, default="PENDING")

    def publish(self):
        if self.published_status=="PUBLISHED":
            self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class ApplicationForm(models.Model):
    title = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.user')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    notice_period = models.CharField(max_length=10)
    applied_date = models.DateTimeField(blank=True, null=True)
    upload_resume = models.FileField()

    def apply(self):
        self.applied_date = timezone.now()
        self.save()

    def __str__(self):
        return "You have successfully applied for the job - " + str(self.title)
