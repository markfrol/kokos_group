from django.shortcuts import render
from .models import ExchangeRate, Currency


def show_rates(request):
    date = request.GET.get("date")
    rates = ExchangeRate.objects.filter(date=date).select_related("currency")
    return render(
        request, "main/show_rates.html", {"rates": rates, "selected_date": date}
    )
