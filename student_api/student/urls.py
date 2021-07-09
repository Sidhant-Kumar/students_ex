from django.conf.urls import url
from student_api.student import views

urlpatterns = [
        url(r'^api/students$', views.student_list),
        url(r'^api/students/(?P<pk>[0-9]+)$', views.student_details),
        url(r'^api/students_list$', views.student_list_published)
]