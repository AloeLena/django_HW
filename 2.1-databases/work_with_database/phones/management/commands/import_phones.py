import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            new_phone = Phone(
                name=phone['name'],
                price=float(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=(phone['lte_exists'] == 'true'),
            )

            new_phone.save()

            self.stdout.write(self.style.SUCCESS(f'Телефон успешно добавлен: {new_phone.name}'))