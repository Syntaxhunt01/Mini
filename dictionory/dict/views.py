from django.shortcuts import render
import requests

# Create your views here.

def dictionary_view(request):
    result = None
    error = None


    if request.method == 'POST':
        word = request.POST.get('word')
        api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

        response = requests.get(api_url)


        if response.status_code == 200:
            data = response.json()
        
            try:
                result = {
                    'word': word,
                    'phonetics': data[0]['phonetics'][0].get('text', ''),
                    'audio': data[0]['phonetics'][0].get('audio', ''),
                    'definition': data[0]['meanings'][0]['definitions'][0]['definition'],
                    'part_of_speech': data[0]['meanings'][0]['partOfSpeech'],
                    'example': data[0]['meanings'][0]['definitions'][0].get('example', '')
                }
            except:
                error = "Result parsing error."

        else:
            error = "Word not found"

    return render(request, 'index.html', {'result': result, 'error': error})