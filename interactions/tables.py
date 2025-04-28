import django_tables2 as tables
from .models import Interaction
from django.utils.html import format_html
from django.urls import reverse
from django.template.loader import render_to_string

class InteractionTable(tables.Table):
    full_name = tables.Column(accessor='contact.get_full_name', verbose_name='Full Name')
    company_name = tables.Column(accessor='contact.company.name', verbose_name='Company Name')
    industry = tables.Column(accessor='contact.company.industry', verbose_name='Industry ')
    address = tables.Column(accessor='contact.company.address', verbose_name='Address')
    full_name = tables.Column(verbose_name='Full Name')
    email = tables.Column(accessor='contact.email', verbose_name='Email')
    phone_number = tables.Column(accessor='contact.phone_number', verbose_name='Phone Number')
    job_title = tables.Column(accessor='contact.job_title', verbose_name='Job Title')
    department = tables.Column(accessor='contact.department', verbose_name='Department')
    last_interaction = tables.Column(empty_values=(), verbose_name='Last Interaction')
    actions = tables.Column(empty_values=(), verbose_name='Action')
    class Meta:
        model = Interaction
        template_name = "django_tables2/bootstrap4.html" 
        fields = ("company_name", "industry","address","full_name", "email", "phone_number", "job_title","department", "last_interaction")
    
    
    def render_actions(self, record):
        add_interaction_url = reverse('interactions:add_interaction', args=[record.pk])
        interaction_detail_url = reverse('interactions:interaction_detail', args=[record.pk])

        call_button = format_html('<a href="{}" class="btn btn-primary btn-sm">Call</a>', add_interaction_url)
        detail_button = format_html('<a href="{}" class="btn btn-secondary btn-sm">Details</a>', interaction_detail_url)

        return format_html('{} {}', call_button, detail_button)
    
    
    # def render_last_interaction(self, record):
    #     last_interaction = self.interactions_date.last()
    #     last_interaction = record.get_last_interaction()

    #     if last_interaction:
    #         call_notes = last_interaction.call_notes
    #         # Create a unique ID for the modal to differentiate between Interactions
    #         modal_id = f"callNotesModal-{record.pk}"

    #         # Button to trigger the modal
    #         button_html = format_html(
    #             '<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#{}">Show Notes</button>',
    #             modal_id
    #         )

    #         # Modal content
    #         modal_content = render_to_string('Interactions/list.html', {'call_notes': call_notes})

    #         # Full HTML with modal trigger button and modal content
    #         result_html = format_html('{}<div class="modal fade" id="{}" tabindex="-1" role="dialog" aria-labelledby="{}" aria-hidden="true">{}</div>',
    #                                   button_html, modal_id, modal_id, modal_content)
    #     else:
    #         result_html = ''

    #     return result_html