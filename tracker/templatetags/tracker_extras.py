from django import template
from tracker.models import Project_Info

register = template.Library()

@register.inclusion_tag('tracker/projectlist.html')
def get_project_list(project=None):
	return {'Projects': Project_Info.objects.all().order_by("Project_Name"), 'act_project': project}
