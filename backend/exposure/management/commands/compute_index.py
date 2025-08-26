from django.core.management.base import BaseCommand
from ...services.analysis import run_analysis


class Command(BaseCommand):
    help = 'Run exposure index computation using synthetic data'

    def handle(self, *args, **options):
        import numpy as np
        layer_data = {
            'temperature': np.random.rand(5, 5),
            'vegetation': np.random.rand(5, 5),
        }
        weights = {'temperature': 0.5, 'vegetation': 0.5}
        count = run_analysis(layer_data, weights)
        self.stdout.write(f'Created {count} exposure polygons')
