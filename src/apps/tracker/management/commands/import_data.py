import csv
from django.core.management.base import BaseCommand

#import model
from apps.tracker.models import FoodAdvice  # Import your model

#import food advice data into database
class Command(BaseCommand):
    help = 'Import data from a CSV file into the MyModel table'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                FoodAdvice.objects.create(
                    food_id = row['food_id'],
                    category_name = row['category_name'],
                    name = row['name'],
                    name_subtitle = row['name_subtitle'],
                    keywords = row['keywords'],
                    pantry_max_days = row['pantry_max_days'],
                    pantry_tips = row['pantry_tips'],
                    fridge_needed = row['fridge_needed'],
                    refrigerate_max_days = row['refrigerate_max_days'],
                    refrigerate_ao_max_days = row['refrigerate_ao_max_days'],
                    freeze_recommended = row['freeze_recommended'],
                    refrigerate_tips = row['refrigerate_tips'],    
                    compost = row['compost'],
                    food_waste_index = row['food_waste_index']
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
