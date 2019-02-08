from django.db import models

# Create your models here.
class Patient(models.Model):
	name = models.CharField(max_length=30)
	pid = models.IntegerField(blank=True, null=True)
	symptoms = models.TextField(blank=True, null=True)
	weight = models.IntegerField(null=False)
	prescriptions = models.CharField(max_length=500)
	report = models.FileField()


	def __str__(self):
		return self.pid


