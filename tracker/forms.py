from django.forms import ModelForm
from tracker.models import Project_Stream_Table, CRQtable, Releasetable

class Project_Stream_Table_Form(ModelForm):
	class Meta:
		model = Project_Stream_Table
		fields = ['Project_Stream']
