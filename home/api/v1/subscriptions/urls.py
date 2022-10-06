from django.urls import path
from home.api.v1.subscriptions.views import SubscriptionsAPIViewDetail,SubscriptionsAPIViewList

urlpatterns = [
	path('<int:id>/', SubscriptionsAPIViewDetail.as_view()),
	path('', SubscriptionsAPIViewList.as_view()),	
]