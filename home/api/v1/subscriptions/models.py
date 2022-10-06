from django.db import models

class Subscription(models.Model):
	id = models.AutoField(primary_key=True)
	plan = models.IntegerField()
	app = models.IntegerField()
	active = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)