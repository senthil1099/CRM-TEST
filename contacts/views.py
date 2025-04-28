from django.shortcuts import render, redirect, get_object_or_404
from django_tables2 import RequestConfig
from .models import Contact, Company
from .forms import ContactForm
from .serializers import ContactSerializer
from .tables import ContactTable
from django.contrib.auth.decorators import login_required

@login_required
def contact_list(request):
    contact = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contact': contact})

@login_required
def contact_detail(request, company_id):
    # contact_id = get_object_or_404(Contact, id=company_id)
    instance = Contact.objects.filter(company_id=company_id)
    serializer = ContactSerializer(instance, many=True)
    return render(request, 'contacts/contact_detail.html', {'serializer_data': serializer.data})

@login_required
def add_contact(request, pk):
    company = get_object_or_404(Company, pk=pk)

    if request.method == 'POST':
        data = request.POST
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.validated_data['company'] = company
            serializer.save()
            return redirect('contacts:list')
    else:
        serializer = ContactSerializer()

    companies = Company.objects.all()

    return render(request, 'contacts/add_contact.html', {'serializer': serializer, 'companies': companies, 'selected_company': company})

@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        data = request.POST
        serializer = ContactSerializer(instance=contact, data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('contacts:contact_list')
        else:
            print(serializer.errors)
    else:
        serializer = ContactSerializer(instance=contact)

    companies = Company.objects.all() 

    return render(request, 'contacts/add_contact.html', {'serializer_data': serializer.data, 'companies': companies, 'editing': True, 'contact_id': contact_id})

@login_required
def list(request):
    queryset = Contact.objects.all()
    table = ContactTable(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'contacts/list.html', {'table': table})
