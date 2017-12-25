from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

import os

class Command(BaseCommand):
  help = 'Configure the application'

  def add_arguments(self, parser):
    pass

  def handle(self, *args, **options):
    # We aren't keeping track of the database through version control, so we
    # want to make sure when we update the database with any migrations added
    # in version control or create the database if it's not there in the first
    # place. Performing the migration should accomplish this.
    self.stdout.write("Performing database migration...")
    call_command("migrate")
    self.stdout.write("Database migration complete.")

    self.stdout.write(os.linesep)

    # We're also ignoring the collected static files. These can easily be
    # copied at deploy time, so we do that here.
    self.stdout.write("Collecting static files...")
    call_command("collectstatic", "--no-input")
    self.stdout.write("Static file collected.")
    
    self.stdout.write("Configuration complete.")
