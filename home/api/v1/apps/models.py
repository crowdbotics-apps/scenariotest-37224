from django.db import models

class App(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=500)
	type = models.CharField(max_length=100)
	framework = models.CharField(max_length=100)
	domain_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)