from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Avtomobil
from .forms import AvtomobilForm


# Avtomobillar ro'yxati
def avtomobillar_royxati(request):
    avtomobillar = Avtomobil.objects.select_related('kategoriya').all()
    return render(request, 'avtomobillar/royxat.html', {
        'avtomobillar': avtomobillar
    })


class AvtomobilListView(ListView):
    model = Avtomobil
    template_name = 'avtomobillar/royxat.html'
    context_object_name = 'avtomobillar'


# Bitta avtomobilni ko'rsatish
def avtomobil_detail(request, id):
    try:
        avtomobil = Avtomobil.objects.prefetch_related('rasmlar').get(id=id)
    except Avtomobil.DoesNotExist:
        return redirect('avtomobillar_royxati')

    return render(request, 'avtomobillar/detail.html', {
        'avtomobil': avtomobil
    })


def avtomobil_qoshish(request):
    if request.method == 'POST':
        form = AvtomobilForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('avtomobillar_royxati')
    else:
        form = AvtomobilForm()

    return render(request, 'avtomobillar/avtomobil_form.html', {
        'form': form
    })