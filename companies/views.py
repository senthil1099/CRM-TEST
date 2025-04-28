from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompanyForm
from .models import Company
from contacts.models import Contact
from interactions.models import Interaction
from .serializers import CompanySerializer
from contacts.serializers import ContactSerializer
from interactions.serializers import InteractionSerializer
from django.contrib.auth.decorators import login_required

@login_required
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/company_list.html', {'companies': companies})

@login_required
def company_detail(request, pk):
    instance = Company.objects.get(pk=pk)
    instances = Contact.objects.filter(pk=pk)
    instancess = Interaction.objects.filter(pk=pk)
    serializer = CompanySerializer(instance)
    serializers = ContactSerializer(instances, many = True)
    serializerss = InteractionSerializer(instancess, many = True)
    return render(request, 'companies/company_detail.html', {'serializer_data': serializer.data,'serializers_data': serializers.data ,'serializerss_data': serializerss.data })


@login_required
def add_company(request):
    if request.method == 'POST':
        data = request.POST
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/companies/list')
    else:
        serializer = CompanySerializer()

    return render(request, 'companies/add_company.html', {'serializer': serializer})


@login_required
def edit_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if request.method == 'POST':
        data = request.POST
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/companies/list')
    else:
        serializer = CompanySerializer(instance=company)

    return render(request, 'companies/add_company.html', {'serializer_data': serializer.data, 'company': company, 'editing': True})