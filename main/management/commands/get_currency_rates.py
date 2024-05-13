from django.core.management.base import BaseCommand
import requests
from main.models import ExchangeRate, Currency
from datetime import datetime


class Command(BaseCommand):
    help = "Get and save currency rates"

    def handle(self, *args, **options):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        try:
            response = requests.get(url)
            data = response.json()

            for currency_code, currency_data in data["Valute"].items():
                currency, created = Currency.objects.get_or_create(
                    char_code=currency_code, name=currency_data["Name"]
                )
                date_str = data["Date"].split("T")[0]
                exchange_rate, created = ExchangeRate.objects.get_or_create(
                    currency=currency,
                    date=datetime.strptime(date_str, "%Y-%m-%d").date(),
                    defaults={"value": currency_data["Value"]},
                )
                if not created:
                    exchange_rate.value = currency_data["Value"]
                    exchange_rate.save()
        except BaseException:
            self.stdout.write(self.style.ERROR("Failed to update currency rates"))
        else:
            self.stdout.write(
                self.style.SUCCESS("Currency rates have been successfully updated")
            )
