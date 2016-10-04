from django.conf.urls import url, include
from . import views


app_name = 'dashboard'


urlpatterns = [
	 url(r'^$', views.index, name='index'),
	 url(r'^about-us/$', views.aboutus, name='aboutus'),
	 url(r'^about-us-with-team-members/$', views.about_us_with_team_members, name='about_us_with_team_members'),
	 url(r'^service/$', views.service, name='service'),
	 url(r'^portfolio-2-column-with-caption/$', views.portfolio, name='portfolio'),
	 url(r'^blogs/$', views.blogs, name='blogs'),
	 url(r'^shop/$', views.shop, name='shop'),
	 url(r'^contact-us/$', views.contact, name='contact'),
	 
]