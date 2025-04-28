from django.shortcuts import render, redirect, get_object_or_404
from .models import Interaction,Contact
from .serializers import InteractionSerializer
from django.contrib.auth.decorators import login_required
from .tables import InteractionTable
from django_tables2 import RequestConfig

@login_required
def add_interaction(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        data = request.POST
        serializer = InteractionSerializer(data=data, context={'request': request, 'contact_id': contact_id})
        if serializer.is_valid():
            serializer.validated_data['contact'] = contact
            interaction = serializer.save(user=request.user)
            # contact.last_interaction = interaction
            contact.save()
            return redirect('contacts:list')
    else:
        serializer = InteractionSerializer()

    return render(request, 'interactions/add_interaction.html', {'serializer': serializer})

@login_required
def interaction_detail(request, contact_id):
    contact_instance = get_object_or_404(Contact, pk=contact_id)
    interactions = contact_instance.interaction_set.all().order_by('-interaction_date')
    interactions_data = InteractionSerializer(interactions, many=True).data

    return render(request, 'interactions/interaction_detail.html', {'interactions_data': interactions_data})


@login_required
def list(request):
    queryset = Interaction.objects.all()
    table = InteractionTable(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'interactions/list.html', {'table': table})
