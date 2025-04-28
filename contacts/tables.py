import django_tables2 as tables
from .models import Contact
from django.utils.html import format_html
from django.urls import reverse
from django.template.loader import render_to_string

class ContactTable(tables.Table):
    full_name = tables.Column(accessor='get_full_name', verbose_name='Full Name')
    company_name = tables.Column(accessor='company.name', verbose_name='Company Name')
    industry = tables.Column(accessor='company.industry', verbose_name='Industry ')
    address = tables.Column(accessor='company.address', verbose_name='Address')
    full_name = tables.Column(verbose_name='Full Name')
    email = tables.Column(accessor='email', verbose_name='Email')
    phone_number = tables.Column(accessor='phone_number', verbose_name='Phone Number')
    job_title = tables.Column(accessor='job_title', verbose_name='Job Title')
    department = tables.Column(accessor='department', verbose_name='Department')
    actions = tables.Column(empty_values=(), verbose_name='Action')
    class Meta:
        model = Contact
        template_name = "django_tables2/bootstrap4.html" 
        fields = ("company_name", "industry","address","full_name", "email", "phone_number", "job_title","department")
    
    
    def render_actions(self, record):
        add_interaction_url = reverse('interactions:add_interaction', args=[record.pk])
        interaction_detail_url = reverse('interactions:interaction_detail', args=[record.pk])

        call_button = format_html('<a href="{}" class="btn btn-primary btn-sm">Call</a>', add_interaction_url)
        detail_button = format_html('<a href="{}" class="btn btn-secondary btn-sm">Details</a>', interaction_detail_url)

        return format_html('{} {}', call_button, detail_button)
    
    
