import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-fill'
        )

    def handle(self, *args, **options):
        with open('phons.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            print(phone)
            phone_ = Phone()
            phone_.name = phone['name']
            phone_.price = float(phone['price'])
            phone_.image = phone['image']
            phone_.release_date = phone['release_date']
            phone_.lte_exists = phone['lte_exists']
            phone_.slug = slugify(phone_.name)
            phone_.save()