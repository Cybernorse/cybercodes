from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.employee_form,name='emp_add'),
    path('<int:id>/', views.employee_form,name="emp_update"),
    path('delete<int:id>/',views.employee_delete,name='emp_delete'),
    path('list/',views.employee_list,name="emp_list")
]
