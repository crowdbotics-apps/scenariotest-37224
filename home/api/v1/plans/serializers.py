from rest_framework import serializers
from home.api.v1.plans.models import Plan


class PlansSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plan
		fields = '__all__'