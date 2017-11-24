import csv

from django.core.management.base import BaseCommand, CommandError
from django.db import connection

from .tabledata import tabledata, to_string



class Command(BaseCommand):
    help = 'Drop selected testdbs'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('tables', nargs='*', type=str)
                    
    def drop(self, dbname):
        _DropSQL = "DROP TABLE {}"

        c = connection.cursor()
        success = False
        try:
            c.execute(_DropSQL.format(dbname))
            success = True
        finally:
            c.close()
        return success

    def print_dbs(self):
        self.stdout.write(to_string())
        
    def handle(self, *args, **options):
        if (not options['tables']):
            self.print_dbs()
            return
        for table in options['tables']:
            try:
              model = tabledata[table].model
            except KeyError:
                self.stdout.write('db table "{0}" not available (try run "populate" with no commands)'.format(
                table
                ))
                continue
            table_name = model._meta.db_table
            if(self.drop(table_name)):
                self.stdout.write('table "{}" dropped'.format(table))
            else:
                self.stdout.write('table "{}" failed to drop?'.format(table))
        self.stdout.write('Done')
         
    
