from django.core.management.base import BaseCommand

from schemas.models import ProcessingStatus


class Command(BaseCommand):
    help = 'Populate database with processing statuses.'

    def handle(self, *args, **kwargs):
        statuses = ['Success', 'Processing']

        for status in statuses:
            ProcessingStatus.objects.create(state=status)

        self.stdout.write(f'{len(statuses)} statuses added.')
