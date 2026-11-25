from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Avtomobil, Kategoriya, AvtomobilRasmi


# Bir vaqtda bir nechta fayl tanlash uchun maydon
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_clean(d, initial) for d in data]
        else:
            result = [single_clean(data, initial)]
        return [f for f in result if f]


class AvtomobilAdminForm(forms.ModelForm):
    galereya = MultipleFileField(
        required=False,
        label="Galereya rasmlari",
        help_text="Bir nechta rasmni birdan tanlang (Ctrl yoki Shift bilan). "
                  "Turini keyin 'Avtomobil rasmlari' tabida o'zgartirish mumkin."
    )

    class Meta:
        model = Avtomobil
        fields = '__all__'


class AvtomobilRasmiInline(admin.TabularInline):
    model = AvtomobilRasmi
    extra = 1
    fields = ('rasm', 'turi', 'rasm_korish')
    readonly_fields = ('rasm_korish',)
    show_change_link = True

    def rasm_korish(self, obj):
        if obj and obj.pk and obj.rasm:
            return format_html(
                '<img src="{}" width="120" height="80" '
                'style="object-fit:cover; border-radius:8px;" />',
                obj.rasm.url
            )
        return "Rasm yuklanmagan"

    rasm_korish.short_description = "Rasm ko‘rinishi"


@admin.register(Avtomobil)
class AvtomobilAdmin(admin.ModelAdmin):
    form = AvtomobilAdminForm
    list_display = ('marka', 'model', 'yil', 'narx', 'kategoriya')
    inlines = [AvtomobilRasmiInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for fayl in form.cleaned_data.get('galereya') or []:
            AvtomobilRasmi.objects.create(
                avtomobil=form.instance,
                rasm=fayl,
                turi='tashqi',
            )


@admin.register(Kategoriya)
class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi')


@admin.register(AvtomobilRasmi)
class AvtomobilRasmiAdmin(admin.ModelAdmin):
    list_display = ('avtomobil', 'turi')