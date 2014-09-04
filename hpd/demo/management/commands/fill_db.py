from django.core.management.base import BaseCommand, CommandError
from hpd.demo.utils import fake_profile


class Command(BaseCommand):
    args = '<number>'
    help = 'Creates [number] records in the database'

    def handle(self, *args, **options):
        try:
            number = int(args[0])
        except (IndexError, ValueError):
            number = 1000
        for i in range(number):
            profile = fake_profile
            self.stdout.write("Hello {}".format(profile.name))
