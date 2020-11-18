from django.shortcuts import render, redirect
from .models import Doador
from .forms import DoadorForm

def list_doador(request):
    doador = Doador.objects.all()
    return render(request, 'doador.html', {'doador': doador})

def create_doador(request):
    form = DoadorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_doador')

    return render(request, 'doador-form.html', {'form': form})


def update_doador(request, id):
    doador = Doador.objects.get(id=id)
    form = DoadorForm(request.POST or None, instance=doador)

    if form.is_valid():
        form.save()
        return redirect('list_doador')

    return render(request, 'doador-form.html', {'form': form, 'doador': doador})


def delete_doador(request, id):
    doador = Doador.objects.get(id=id)

    if request.method == 'POST':
        doador.delete()
        return redirect('list_doador')

    return render(request, 'doador-delete-confirm.html', {'doador': doador})