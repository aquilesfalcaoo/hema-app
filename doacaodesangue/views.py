from django.shortcuts import render, redirect
from .models import Doador
from .forms import DoadorForm
from .models import Medico
from .forms import MedicoForm

def list_donor(request):
    donors = Doador.objects.all()
    return render(request, 'donor.html', {'donors': donors})

def create_donor(request):
    form = DoadorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_donor')

    return render(request, 'donor-form.html', {'form': form})


def update_donor(request, id):
    donors = Doador.objects.get(id=id)
    form = DoadorForm(request.POST or None, instance=donors)

    if form.is_valid():
        form.save()
        return redirect('list_donor')

    return render(request, 'donor-form.html', {'form': form, 'donors': donors})


def delete_crime(request, id):
    donors = Doador.objects.get(id=id)

    if request.method == 'POST':
        donors.delete()
        return redirect('list_donor')

    return render(request, 'donor-delete-confirm.html', {'donors': donors})