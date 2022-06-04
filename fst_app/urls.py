from django.urls import path
from fst_app import views

app_name ='fst_app'

urlpatterns = [
 
    path('',views.index,name='index'),
    path('stu/',views.student,name='student'),
    path('student_info/<int:student_id>/',views.stuinfo,name='stuinfo'),
    path('stu_update/<int:student_id>/',views.stuup,name='stuup'),
    path('stu_dlt/<int:student_id>/',views.studlt, name ='studlt'),
]
