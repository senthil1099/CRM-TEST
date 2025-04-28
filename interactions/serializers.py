from rest_framework import serializers
from .models import Interaction, Contact




class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'

    
    def create(self, validated_data):
        user = self.context['request'].user 
        validated_data['user'] = user
        contact_id = self.context['contact_id']
        contact = Contact.objects.get(id=contact_id)
        validated_data['contact'] = contact

        interaction = Interaction.objects.create(**validated_data)
        return interaction