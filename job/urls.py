from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.job_list, name='job_list'),
    url(r'^job/(?P<pk>\d+)/$', views.job_detail, name='job_detail'),
    url(r'^job/(?P<pk>\d+)/apply_job/$', views.apply_job, name='apply_job'),
    url(r'^job/(?P<pk>\d+)/register_naukri/$', views.register_naukri, name='register_naukri'),
    url(r'^admin/dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^job/create_job/$', views.create_job, name='create_job'),

]