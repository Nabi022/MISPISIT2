from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from .forms import RecordForm

def index(request):
    records = Record.objects.all()
    return render(request, 'home/index.html', {'records': records})

def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecordForm()
    return render(request, 'home/form.html', {'form': form})

def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecordForm(instance=record)
    return render(request, 'home/form.html', {'form': form})

def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('home')
    return render(request, 'home/delete.html', {'record': record})
