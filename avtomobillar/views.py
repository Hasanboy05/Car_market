
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Avtomobil


# 3-topshiriq: Function-based view
def avtomobillar_royxati(request):
    avtomobillar = Avtomobil.objects.all()
    return render(request, 'avtomobillar/royxat.html', {
        'avtomobillar': avtomobillar
    })


# Avvalgi ListView
class AvtomobilListView(ListView):
    model = Avtomobil
    template_name = 'avtomobillar/royxat.html'
    context_object_name = 'avtomobillar'


# 4-topshiriq: Bitta avtomobilni ko'rsatish
def avtomobil_detail(request, id):
    avtomobil = get_object_or_404(Avtomobil, id=id)
    return render(request, 'avtomobillar/detail.html', {
        'avtomobil': avtomobil
    })
