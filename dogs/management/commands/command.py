from dogs.models import Dog, Categories
from django.core.management import BaseCommand
from django.core.management import call_command
class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('dumpdata', 'dogs', output='data.json')
        Dog.objects.all().delete
        Categories.objects.all().delete
        call_command('loaddata', 'data.json')