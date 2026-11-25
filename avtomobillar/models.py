
from django.db import models


class Kategoriya(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi


class Avtomobil(models.Model):

    VALYUTA_TANLOV = [
        ('UZS', "So'm"),
        ('USD', 'Dollar ($)'),
    ]

    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    yil = models.PositiveIntegerField()
    narx = models.DecimalField(max_digits=12, decimal_places=2)

    valyuta = models.CharField(
        max_length=3,
        choices=VALYUTA_TANLOV,
        default='UZS'
    )

    rasm = models.ImageField(
        upload_to='avtomobillar/',
        blank=True,
        null=True
    )

    # Yangi ma'lumotlar
    yurgan_masofa = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Kilometr hisobida"
    )

    yoqilgi_turi = models.CharField(
        max_length=50,
        blank=True
    )

    rangi = models.CharField(
        max_length=50,
        blank=True
    )

    telefon = models.CharField(
        max_length=20,
        blank=True
    )

    telegram = models.CharField(
        max_length=100,
        blank=True,
        help_text="Telegram username, masalan: @username"
    )

    kategoriya = models.ForeignKey(
        Kategoriya,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='avtomobillar'
    )

    def __str__(self):
        return f"{self.marka} {self.model}"


# Avtomobil uchun bir nechta rasm
class AvtomobilRasmi(models.Model):

    RASM_TURLARI = [
        ('tashqi', 'Tashqi ko‘rinishi'),
        ('ichki', 'Ichki salon'),
        ('shina', 'Shinalar va disklar'),
    ]

    avtomobil = models.ForeignKey(
        Avtomobil,
        on_delete=models.CASCADE,
        related_name='rasmlar'
    )

    rasm = models.ImageField(
        upload_to='avtomobillar/galereya/'
    )

    turi = models.CharField(
        max_length=20,
        choices=RASM_TURLARI,
        default='tashqi'          # <-- qo'shildi
    )

    class Meta:                    # <-- qo'shildi
        verbose_name = "Avtomobil rasmi"
        verbose_name_plural = "Avtomobil rasmlari"

    def __str__(self):
        return f"{self.avtomobil} - {self.get_turi_display()}"
