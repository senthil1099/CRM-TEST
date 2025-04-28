from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact/<int:company_id>/', views.contact_detail, name='contact_detail'),
    path('add-contact/<int:pk>/',views.add_contact, name='add_contact' ),
    path('edit/<int:contact_id>/',views.edit_contact, name='edit_contact'),
    path('contact-list/', views.contact_list, name='contact_list'),
    path('list/', views.list, name='list'),
]
