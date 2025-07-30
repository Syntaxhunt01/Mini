
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import random
from django.views.decorators.csrf import csrf_exempt


def random_quote(request):
    quotes = Quote.objects.all()
    quote = random.choice(quotes) if quotes else None
    return render(request, 'quote.html', {'quote': quote})


def api_random_quote(request):
    quotes = Quote.objects.all()
    if not quotes:
        return JsonResponse({'error': 'No quotes found.'}, status=404)
    quote = random.choice(quotes)
    return JsonResponse({
        'text': quote.text,
        'author': quote.author
    })


@csrf_exempt
def add_quote(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.POST.get('author')
        if text and author:
            Quote.objects.create(text=text, author=author)
            return JsonResponse({'message': 'Quote added sucssesfully.'})
        else:
            return JsonResponse({'error': 'Missing fields'}, status=400)
        
    return render(request, 'add_quote.html')