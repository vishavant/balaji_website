from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .forms import ContactUsForm
from django.contrib import messages
from .models import ContactUs
# Create your views here.

def homepage(request):
    return render(request, "website/homepage.html")



def index(request):
    return render(request, "website/index.html")


def create_contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact created successfully.')
            return redirect('website:contact_list') 
    else:
        form = ContactUsForm()

    return render(request, 'website/contact_us.html', {'form': form})



def contact_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def update_contact(request, contact_id):
    contact = get_object_or_404(ContactUs, contact_id=contact_id)

    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated successfully.')
            return redirect('contact_list')  # Redirect to contact list view
    else:
        form = ContactUsForm(instance=contact)

    return render(request, 'update_contact.html', {'form': form, 'contact': contact})


def delete_contact(request, contact_id):
    contact = get_object_or_404(ContactUs, contact_id=contact_id)
    contact.delete()
    messages.success(request, 'Contact deleted successfully.')
    return redirect('contact_list')



def about_us(request):
    return render(request, "website/about.html")


def portfolio(request):
    return render(request, "website/portfolio.html")