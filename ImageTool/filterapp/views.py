from django.shortcuts import render
from .forms import *
from PIL import Image, ImageFilter
import os
from django.conf import settings
import uuid



def filter_image_view(request):
    if request.method == 'POST':
        form = ImageFilterForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(request.FILES['image'])
            filter_type = form.cleaned_data['filter_type']


            if filter_type == 'BLUR':
                image = image.filter(ImageFilter.BLUR)
            if filter_type == 'BW':
                image = image.convert('L')
            if filter_type == 'SHARPEN':
                image = image.filter(ImageFilter.SHARPEN)
            if filter_type == 'CONTOUR':
                image = image.filter(ImageFilter.CONTOUR)

            filename = f"{uuid.uuid4().hex}.png"
            save_path = os.path.join(settings.MEDIA_ROOT, 'filtered', filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            image.save(save_path)

            return render(request, 'filter_result.html',{
                'filter_url': f"/media/filtered/{filename}"
            })
    else:
        form = ImageFilterForm()
    return render(request, 'upload_image.html', {'form': form})
