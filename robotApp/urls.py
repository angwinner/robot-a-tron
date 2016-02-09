'''
Created on Jan 28, 2016

@author: awinner
'''
from django.conf.urls import url
from . import views #this is the nicer way the django doc uses

urlpatterns = [
        url(r'^$', views.robot_index),
        url(r'^add$', views.add_robot, name = 'add_robot'),
        url(r'^(?P<pk>\d+)/edit$', views.edit_robot, name = 'edit_robot'),
        url(r'^(?P<pk>\d+)/delete$', views.delete_robot, name = 'delete_robot')
]
