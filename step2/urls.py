from django.conf.urls import url 
from step2 import views

urlpatterns = [ 
	url(r'^about/',views.about, name='about'),
	url(r'^viewcourier/(?P<loc_to>\w)/$', views.view_courier, name='view_courier'),
	url(r'^request_made/$', views.req_made, name='req_made'),
]
