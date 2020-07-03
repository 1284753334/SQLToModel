from django.conf.urls import url

from . import  views

app_name = 'app'

urlpatterns = [
    url(r'^index/',views.index, name='index'),
    url(r'^upload/',views.upload,name = 'upload'),
    url(r'^imgfield/',views.imgfield,name = 'imgfield'),
    url(r'^mine/',views.mine,name = 'mine'),

]