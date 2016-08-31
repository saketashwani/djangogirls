from django.shortcuts import render
from tracker.models import Project_Info, Project_Stream_Table


def home(request):
	context_param = {}
	#projects = Project_Info.objects.all().order_by("Project_Name")
	#context_param['projects'] = projects

	return render(request, 'tracker/home.html', context_param)

def project_summary(request, project_sname):
	context_param = {}
	print (project_sname)

	try:
		project = Project_Info.objects.get(Project_Short_Name=project_sname)
		context_param['project'] = project

		streams = Project_Stream_Table.objects.filter(Project_Short_Name = project)
		context_param['streams'] = streams

	except Project_Info.DoesNotExist:
		pass

	return render(request, 'tracker/project_summary.html', context_param) 
