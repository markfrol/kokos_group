from django.db import models


class Currency(models.Model):
    char_code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.currency} - {self.date}"

    class Meta:
        verbose_name = "Курс валюты"
        verbose_name_plural = "Курсы валют"
