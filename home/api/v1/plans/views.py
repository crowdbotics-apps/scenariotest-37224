from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from home.api.v1.plans.models import Plan
from home.api.v1.plans.serializers import PlansSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

class PlansAPIViewList(APIView):
	serializer_class = PlansSerializer

	@swagger_auto_schema(responses={200: PlansSerializer(many=True)})
	def get(self, request):

		plans = Plan.objects.all()

		if plans:
			plan_serializer = self.serializer_class(plans, many=True)
			return Response(plan_serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({'message':'No plans found'}, status=status.HTTP_200_OK)

class PlansAPIViewDetail(APIView):
	serializer_class = PlansSerializer
	
	@swagger_auto_schema(responses={200: PlansSerializer(many=True)})
	def get(self, request):
		
		plan_id = request.query_params.get('id', None)

		plans = None

		if plan_id:
			plans = Plan.objects.filter(id=plan_id)

		if plans:
			plan_serializer = self.serializer_class(plans, many=True)
			return Response(plan_serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({'message':'No plans found'}, status=status.HTTP_200_OK)