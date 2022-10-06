from django.urls import path
from home.api.v1.plans.views import PlansAPIViewList,PlansAPIViewDetail

urlpatterns = [
	path('', PlansAPIViewList.as_view()),
	path('<int:id>/', PlansAPIViewDetail.as_view()),	
]