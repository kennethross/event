import os
import csv
from django.conf import settings
from submit.models import Invite
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
			print "Loading CSV"
			csv_path = os.path.join(settings.BASE_DIR, "a.csv")
			print csv_path
			csv_file = open(csv_path, 'rb')
			csv_reader = csv.DictReader(csv_file)
			for row in csv_reader:
			
				##if len(row) == 2:
						obj = Invite.objects.create(
						name=row['name'],
						date=row['date']
            )
			print obj
            


