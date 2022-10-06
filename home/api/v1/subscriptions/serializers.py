from rest_framework import serializers
from home.api.v1.subscriptions.models import Subscription


class SubscriptionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscription
		fields = '__all__'