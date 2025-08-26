from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Stub for ingesting OSM data via Overpass'

    def handle(self, *args, **options):
        self.stdout.write('Ingesting OSM data... (stub)')
