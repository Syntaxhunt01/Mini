from django.shortcuts import render
from .forms import *

# Create your views here.

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'submitted': submitted})

def view_messages(request):
    messages = ContactMessage.objects.all().order_by('-sent_at')
    return render(request, 'messages.html', {'messages': messages})