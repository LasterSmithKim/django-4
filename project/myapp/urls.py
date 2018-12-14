from django.conf.urls import url
from django.urls import path,re_path
from . import views


urlpatterns = [
    re_path(r'^$',views.index),
    re_path(r'^(\d+)/$',views.detail),
    re_path(r'^grades/$',views.grades),
    re_path(r'^students/$',views.students),
    re_path(r'^grades/(\d+)$',views.gradesstudents),
    re_path(r'^addstudent/$',views.addstudent),
    re_path(r'^addstudent1/$',views.addstudent1),
]