from django.db import models

class Location(models.Model):
	location = models.CharField(max_length=255)

	def __str__(self):
		return self.location

class Camera(models.Model):
	camera_name = models.CharField(max_length=255)
	camera_ip = models.CharField(max_length=15)
	input_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='imput_location')
	output_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name='output_location')
	camera_description = models.CharField(max_length=255, null=True, default='null')
	camera_lat = models.FloatField(default=0.0)
	camera_lon = models.FloatField(default=0.0)

	def __str__(self):
		return self.camera_name
	
class GroupType(models.Model):
	type_name = models.CharField(max_length=255)
	
	def __str__(self):
		return self.type_name

class CameraGroup(models.Model):
	group_name = models.CharField(max_length=255)
	group_type = models.ForeignKey(GroupType, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.group_name