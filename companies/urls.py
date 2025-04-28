from django.urls import path
from . import views


app_name = 'companies'

urlpatterns = [
    path('detail/<int:pk>/', views.company_detail, name='company_detail'),
    path('add/',views.add_company, name='add_company' ),
    path('edit/<int:company_id>/',views.edit_company, name='edit_company' ),
    path('list/', views.company_list, name='company_list'),
]
