from django.db import models


class Avtomobil(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    yil = models.PositiveIntegerField()
    narx = models.DecimalField(max_digits=12, decimal_places=2)
    rasm = models.ImageField(upload_to='avtomobillar/', blank=True, null=True)

    def __str__(self):
        return f"{self.marka} {self.model}"