from django.conf.urls import url
from servers import views


urlpatterns = [
    url(r'^$', views.ServerList.as_view(), name='server_list'),
    url(r'^new$', views.ServerCreate.as_view(), name='server_new'),
    url(r'^edit/(?P<pk>\d+)$', views.ServerUpdate.as_view(), name='server_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.ServerDelete.as_view(), name='server_delete'),
]