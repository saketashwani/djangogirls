from django.conf.urls import url
from tracker import views

urlpatterns = [
		url(r'^$',views.home , name='home'),
		url(r'^(?P<project_sname>\w+)/summary$',views.project_summary , name='project_summary'),
		]
