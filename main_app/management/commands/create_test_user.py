from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection

class Command(BaseCommand):
    help = 'Create a test user for Django testing'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("CREATE USER Tester_22 PASSWORD '1234';")
            cursor.execute("GRANT ALL PRIVILEGES ON DATABASE FoliageAnalyst_test_db TO Tester_22;")
        self.stdout.write(self.style.SUCCESS('Test user created successfully.'))
