from django.urls import path
from . import views


app_name = 'interactions'

urlpatterns = [
    path('add-interaction/<int:contact_id>', views.add_interaction, name='add_interaction'),
    path('interaction/<int:contact_id>/', views.interaction_detail, name='interaction_detail'),
    path('list/', views.list, name='list'),
]
