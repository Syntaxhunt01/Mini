from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import *
from .forms import *

def home(request):
    query = request.GET.get('q')
    notes = Note.objects.filter(title__icontains=query) if query else Note.objects.all().order_by('-created_at')

    return render(request, 'home.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoteForm()

    return render(request, 'add_note.html', {'form': form})

def edit_note(requset, note_id):
    note = get_object_or_404(Note, id=note_id)
    if requset.method == 'POST':
        form = NoteForm(requset.POST, instance=note)
        if form.is_vaild():
            form.save()
            return redirect('/')
        
    else:
        form = NoteForm(instance=note)

    return render(requset, 'edit.html', {'form': form, 'note': note})


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('/')