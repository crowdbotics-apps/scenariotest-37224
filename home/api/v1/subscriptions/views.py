from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from home.api.v1.subscriptions.models import Subscription
from home.api.v1.subscriptions.serializers import SubscriptionsSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING,TYPE_INTEGER, TYPE_BOOLEAN

class SubscriptionsAPIViewList(APIView):
	serializer_class = SubscriptionsSerializer

	subscriptions_schema = Schema(
		type=TYPE_OBJECT,
		properties={
			'plan': Schema(type=TYPE_INTEGER, description='integer'),
			'app': Schema(type=TYPE_INTEGER, description='integer'),
			'active': Schema(type=TYPE_BOOLEAN, description='boolean'),									
		},
		required=['plan', 'app', 'active']
	)

	subscriptions_schema_put = Schema(
		type=TYPE_OBJECT,
		properties={
			'plan': Schema(type=TYPE_INTEGER, description='integer'),
			'app': Schema(type=TYPE_INTEGER, description='integer'),
			'active': Schema(type=TYPE_BOOLEAN, description='boolean'),								
		},							
	)

	@swagger_auto_schema(responses={200: SubscriptionsSerializer(many=True)})
	def get(self, request):
		
		subscriptions = Subscription.objects.all()

		if subscriptions:
			subscription_serializer = self.serializer_class(subscriptions, many=True)
			return Response(subscription_serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({'message':'No Subscriptions found'}, status=status.HTTP_200_OK)

	@swagger_auto_schema(request_body=subscriptions_schema,responses={200: Schema(type=TYPE_OBJECT,properties={'message': Schema(type=TYPE_STRING, description='string')})})
	def post(self, request):

		plan = request.data.get('plan', None)
		app = request.data.get('app', None)
		active = request.data.get('active', None)

		post_data = {
			'plan': plan,
			'app': app,            
			'active': active
		}

		serializer = self.serializer_class(data=post_data)
		if serializer.is_valid(raise_exception=True):
			app = serializer.save()

		if app:
			return Response({'message': 'Successful new subscription'}, status=status.HTTP_201_CREATED)
		return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionsAPIViewDetail(APIView):
	serializer_class = SubscriptionsSerializer

	subscriptions_schema = Schema(
		type=TYPE_OBJECT,
		properties={
			'plan': Schema(type=TYPE_STRING, description='string'),
			'app': Schema(type=TYPE_STRING, description='string'),
			'active': Schema(type=TYPE_STRING, description='string'),									
		},
		required=['plan', 'app', 'active']
	)

	subscriptions_schema_put = Schema(
		type=TYPE_OBJECT,
		properties={
			'plan': Schema(type=TYPE_STRING, description='string'),
			'app': Schema(type=TYPE_STRING, description='string'),
			'active': Schema(type=TYPE_STRING, description='string'),									
		},							
	)
    
	@swagger_auto_schema(responses={200: SubscriptionsSerializer(many=True)})
	def get(self, request):
		
		subscription_id = request.query_params.get('id', None)
		subscriptions = None
		if subscription_id:
			subscriptions = Subscription.objects.filter(id=subscription_id)

		if subscriptions:
			subscription_serializer = self.serializer_class(subscriptions, many=True)
			return Response(subscription_serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({'message':'No Subscriptions found'}, status=status.HTTP_200_OK)

	@swagger_auto_schema(request_body=subscriptions_schema_put,responses={200: Schema(type=TYPE_OBJECT,properties={'message': Schema(type=TYPE_STRING, description='string')})})
	def put(self, request):
		
		subscription_id = request.query_params.get('id', None)

		subscription = Subscription.objects.get(id=subscription_id)

		if not subscription:
			return Response({'message': 'No subscriptions found'})

		plan = request.data.get('plan', None)
		app = request.data.get('app', None)
		active = request.data.get('active', None)

		plan = request.data.get('plan', None)
		if plan:
			subscription.plan = plan
			subscription.save()

		if app:
			subscription.plan = app
			subscription.save()

		if active:
			subscription.plan = active
			subscription.save()                                      


		return Response({'message': 'Update Complete'}, status=status.HTTP_200_OK)