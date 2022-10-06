from rest_framework import serializers
from home.api.v1.apps.models import App


class AppsSerializer(serializers.ModelSerializer):
	class Meta:
		model = App
		fields = '__all__'