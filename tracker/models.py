from django.db import models


class Project_Info(models.Model):
	Project_Name		= models.CharField(max_length=30, help_text="Project Name")
	Project_Short_Name	= models.CharField(max_length=10, help_text="Project Short Name", primary_key=True)
	Project_Manager		= models.CharField(max_length=30, help_text="Project Manager Name")
	Project_Architect	= models.CharField(max_length=30, help_text="Project Architect Name")

	def __str__(self):
		return self.Project_Name

class Project_Stream_Table(models.Model):
	class Meta:
		unique_together=(('Project_Short_Name','Project_Stream'),)

	#Project_Short_Name			= models.CharField(max_length=10, help_text="Project Short Name", primary_key=True)
	Project_Short_Name			= models.ForeignKey(Project_Info)
	Project_Stream				= models.CharField(max_length=10, help_text="Stream Name")
	Project_Release_Label			= models.CharField(max_length=10, help_text="Release Label")
	Project_Release_Label_Date		= models.DateField(help_text="Released Date",blank=True, null=True)
	Project_Release_Label_inprogress	= models.CharField(max_length=10, help_text="Draft Release Label",blank=True, null=True)
	Project_Release_Label_Date_inprogress	= models.DateField(help_text="Draft Release Date",blank=True, null=True)


	def __str__(self):
		return '%s stream for %s' % (self.Project_Stream , self.Project_Short_Name)
