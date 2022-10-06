from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from home.api.v1.apps.models import App
from home.api.v1.apps.serializers import AppsSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

class AppsAPIViewList(APIView):
	serializer_class = AppsSerializer

	apps_schema = Schema(
		type=TYPE_OBJECT,
		properties={
			'name': Schema(type=TYPE_STRING, description='string'),
			'description': Schema(type=TYPE_STRING, description='string'),
			'type': Schema(type=TYPE_STRING, description='string'),	
			'framework': Schema(type=TYPE_STRING, description='string'),	
			'domain_name': Schema(type=TYPE_STRING, description='string'),								
		},
		required=['name', 'description', 'type', 'framework', 'domain_name']
	)

	apps_schema_put = Schema(
		type=TYPE_OBJECT,
		properties={
			'name': Schema(type=TYPE_STRING, description='string'),
			'description': Schema(type=TYPE_STRING, description='string'),
			'type': Schema(type=TYPE_STRING, description='string'),	
			'framework': Schema(type=TYPE_STRING, description='string'),	
			'domain_name': Schema(type=TYPE_STRING, description='string'),								
		}
	)

	@swagger_auto_schema(responses={200: AppsSerializer(many=True)})
	def get(self, request):
		
		app_id = id

		apps = App.objects.all()

		if apps:
			app_serializer = self.serializer_class(apps, many=True)
			return Response(app_serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({'message':'No apps found'}, status=status.HTTP_200_OK)

	@swagger_auto_schema(request_body=apps_schema,responses={200: Schema(type=TYPE_OBJECT,properties={'message': Schema(type=TYPE_STRING, description='string')})})
	def post(self, request):
	
		name = request.data.get('name', None)
		description = request.data.get('description', None)
		apps_type = request.data.get('type', 'Web')
		framework = request.data.get('framework', 'Django')
		domain_name = request.data.get('domain_name', None)

		post_data = {
			'name': name,
			'description': description,            
			'type': apps_type,
			'framework': framework,
			'domain_name': domain_name
		}

		serializer = self.serializer_class(data=post_data)
		if serializer.is_valid(raise_exception=True):
			app = serializer.save()

		if app:
			return Response({'message': 'Successful new app'}, status=status.HTTP_201_CREATED)
		return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

class AppsAPIViewDetial(APIView):
	serializer_class = AppsSerializer

	apps_schema = Schema(
		type=TYPE_OBJECT,
		properties={
			'name': Schema(type=TYPE_STRING, description='string'),
			'description': Schema(type=TYPE_STRING, description='string'),
			'type': Schema(type=TYPE_STRING, description='string'),	
			'framework': Schema(type=TYPE_STRING, description='string'),	
			'domain_name': Schema(type=TYPE_STRING, description='string'),								
		},
		required=['name', 'description', 'type', 'framework', 'domain_name']
	)

	apps_schema_put = Schema(
		type=TYPE_OBJECT,
		properties={
			'name': Schema(type=TYPE_STRING, description='string'),
			'description': Schema(type=TYPE_STRING, description='string'),
			'type': Schema(type=TYPE_STRING, description='string'),	
			'framework': Schema(type=TYPE_STRING, description='string'),	
			'domain_name': Schema(type=TYPE_STRING, description='string'),								
		}
	)

	@swagger_auto_schema(responses={200: AppsSerializer(many=True)})
	def get(self, request):
		
		app_id = request.query_params.get('id', None)

		apps = App.objects.filter(id=app_id)

		if apps:
			app_serializer = self.serializer_class(apps, many=True)
			return Response(app_serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({'message':'No apps found'}, status=status.HTTP_200_OK)

	@swagger_auto_schema(request_body=apps_schema_put,responses={200: Schema(type=TYPE_OBJECT,properties={'message': Schema(type=TYPE_STRING, description='string')})})
	def put(self, request):
		
		app_id = request.query_params.get('id', None)

		app = App.objects.get(id=app_id)

		if not app:
			return Response({'message': 'No apps found'})

		name = request.data.get('name', None)
		if name:
			app.name = name
			app.save()

		description = request.data.get('description', None)
		if name:
			app.description = description
			app.save()

		app_type = request.data.get('type', None)
		if name:
			app.type = app_type
			app.save()

		framework = request.data.get('framework', None)
		if framework:
			app.framework = framework
			app.save()

		domain_name = request.data.get('domain_name', None)
		if domain_name:
			app.domain_name = domain_name
			app.save()                                   


		return Response({'message': 'Update Complete'}, status=status.HTTP_200_OK)

	@swagger_auto_schema(responses={200: Schema(type=TYPE_OBJECT,properties={'message': Schema(type=TYPE_STRING, description='string')})})
	def delete(self, request):
		
		app_id = request.query_params.get('id', None)
		app = App.objects.get(id=app_id)

		if not app:
			return Response({'message': 'No app found'}, status=status.HTTP_404_NOT_FOUND)

		app.delete()
		return Response({'message': 'App removed'}, status=status.HTTP_200_OK)