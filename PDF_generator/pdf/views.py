import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import uuid
from reportlab.pdfgen import canvas

def generate_pdf_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        image = request.FILES.get('image')

        # Ensure media folder exists
        media_path = os.path.join(settings.MEDIA_ROOT)
        os.makedirs(media_path, exist_ok=True)

        # Save uploaded image
        image_name = f"{uuid.uuid4().hex}.jpg"
        img_path = os.path.join(media_path, image_name)
        
        if image:
            with open(img_path, 'wb+') as dest:
                for chunk in image.chunks():
                    dest.write(chunk)
            
        else:
            return HttpResponse("No Image uploaded", status=400)

        # Create PDF
        pdf_path = os.path.join(media_path, f"{uuid.uuid4().hex}.pdf")
        c = canvas.Canvas(pdf_path)
        c.drawString(100, 800, f"Name: {name}")
        c.drawString(100, 780, f"Email: {email}")
        c.drawString(100, 760, f"Number: {number}")

        # Insert Image
        try:
            c.drawImage(img_path, 100, 500, width=200, height=200)
        except Exception as e:
            c.drawString(100, 740, f"Error loading image: {e}")
        
        c.save()

        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="generated.pdf"'
            return response

    return render(request, 'generate_pdf.html')
