from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def upload_contacts(request):
    if request.method == "POST":
        data = json.loads(request.body)
        contacts = data.get('contacts', [])
        saved = []

        for c in contacts:
            obj, created = Contact.objects.get_or_create(
                phone=c.get('phone'),
                defaults={
                    'name': c.get('name', ''),
                    'email': c.get('email', ''),
                }
            )
            saved.append(obj.phone)

        return JsonResponse({'status': 'success', 'saved_phones': saved})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def scan_number(request):
    if request.method == "POST":
        data = json.loads(request.body)
        number = data.get('number')
        email = data.get('email', None)

        # Check if contact exists by phone
        contact = Contact.objects.filter(phone=number).first()
        if contact:
            return JsonResponse({'match': True, 'name': contact.name, 'email': contact.email})

        # If not found by phone, try by email
        if email:
            email_contact = Contact.objects.filter(email=email).first()
            if email_contact:
                # Save new contact with email's name and phone number
                new_contact = Contact.objects.create(phone=number, name=email_contact.name, email=email)
                return JsonResponse({'match': True, 'name': new_contact.name, 'email': new_contact.email})

        return JsonResponse({'match': False})

    return JsonResponse({'error': 'Invalid request'}, status=400)
