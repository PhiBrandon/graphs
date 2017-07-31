from django.conf.urls import url
from .views import loginView, get_data, ChartData


urlpatterns= [
	url(r'^$', loginView.as_view()),
	url(r'^api/data/$', get_data, name='api-data'),
	url(r'^api/chart/data/$', ChartData.as_view(), name='api-data')

]