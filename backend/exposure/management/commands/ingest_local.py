from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Stub for ingesting local GeoJSON/CSV/SHP data'

    def handle(self, *args, **options):
        self.stdout.write('Ingesting local data... (stub)')
