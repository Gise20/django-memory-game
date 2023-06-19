from django.core.management.base import BaseCommand
from api.models import ConfigNumberCards, ConfigTimeBonus

class Command(BaseCommand):
    help = 'Checks if the table is empty and adds data if needed'

    def handle(self, *args, **options):
        if ConfigNumberCards.objects.count() == 0:
            # Add default data to the ConfigNumberCards table
            ConfigNumberCards.objects.create(Easy=20, Medium=40, Hard=75)
            self.stdout.write(self.style.SUCCESS('ConfigNumberCards data added successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('ConfigNumberCards table is not empty. No action needed.'))

        if ConfigTimeBonus.objects.count() == 0:
            # Add default data to the ConfigTimeBonus table
            ConfigTimeBonus.objects.create(Easy=150, Medium=200, Hard=600)
            self.stdout.write(self.style.SUCCESS('ConfigTimeBonus data added successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('ConfigTimeBonus table is not empty. No action needed.'))
