from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'
