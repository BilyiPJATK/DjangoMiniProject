from django.http import HttpResponse
from django.shortcuts import render

from my_app.forms import ContactForm
from my_app.models import ContactFormSubmission


# Create your views here.
def home_view(request):
    context = {
        'my_title': 'Home Page',
    }
    return render(request, 'home.html', context)

def contact_form_view(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse('Email has been sent')

    return render(request, 'contact.html', {'form': form})

def submission_list_view(request):
    submissions = ContactFormSubmission.objects.all()
    return render(request, 'inbox.html', {'submissions': submissions})