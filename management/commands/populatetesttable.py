import csv
import traceback

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.core.management import call_command

from .tabledata import tabledata, to_string



class Command(BaseCommand):
    help = 'Add data to the testdbs'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('tables', nargs='*', type=str)

    def mkdb(self, data):
        success = False
        with open(data.filepath, 'r') as f:
            reader = csv.reader(f)
            # if a big CSV file creaks, stash useful vars
            idx = -1
            zrow = ()
            try:
                for idx, row in enumerate(reader):
                    # split row into dict
                    zrow = zip(data.fields, row)
                    d = dict(zrow)
                    o = data.model(**d)
                    #if (verbose):
                    #self.stdout.write('.', ending='')
                    o.save()
                success = True
            except Exception as err:
                self.stdout.write('line no:' + str(idx))
                self.stdout.write(str(d))
                #! fix
                #! write error message
                #err.__traceback__.print_tb()
                traceback.print_tb(err.__traceback__, limit=1)
        return (success, idx)

    def print_dbs(self):
        self.stdout.write(to_string())
        
    def handle(self, *args, **options):
        if (not options['tables']):
            self.print_dbs()
            return

        call_command("migrate", '--run-syncdb')

        #self.verbosity
        for table in options['tables']:
            try:
              table_data = tabledata[table]
            except KeyError:
                self.stdout.write('db table "{0}" not available (try run "populate" with no commands)'.format(
                table
                ))
                continue
            count = table_data.model.objects.count()
            if(count > 0):
                self.stdout.write('db table "{0}" must be empty, but is populated with {1} data items?'.format(
                table,
                count
                ))
                continue
            self.stdout.write('Creating db table "{}". This may take some time...'.format(table))
            success, idx = self.mkdb(table_data)
            if(success):
                self.stdout.write('table "{}" populated'.format(table))
            else:
                self.stdout.write('table "{}" failed to populate? Some data may have been written'.format(table))
            self.stdout.write('{} entries written'.format(idx))
        self.stdout.write('Done')
         
    
