from django.contrib.auth.models import User
from django.db import models

class FollowedBill(models.Model):
	"""
	A bill being followed. This is just glue between data.
	"""
	id = models.CharField(max_length=100, primary_key=True)
	followers = models.ManyToManyField(User, related_name='bills',
		blank=True, null=True)

	class Meta:
		pass

	def __unicode__(self):
		return self.id