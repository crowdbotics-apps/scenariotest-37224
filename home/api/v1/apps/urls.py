from django.urls import path, re_path
from home.api.v1.apps.views import AppsAPIViewDetial,AppsAPIViewList

urlpatterns = [
	path('<int:id>/', AppsAPIViewDetial.as_view()),
	path('', AppsAPIViewList.as_view()),	
]