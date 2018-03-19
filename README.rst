Testtable
=========
Don't know why I didn't do this long ago. Yeh for Django.

A note: You must install/remove tables one by one. I don't like to offer the risk you may accidentally uninstall, say, the Stars table when it could take three hours to load (these are only Python scripts)


Note
----
The app runs all the necessary gear to raise and drop some test/example tables. It creates no migrations. Do not run migration commands on the app. If you do by accident, delete the 'migrations' folder.


Install
-------
In settings.py, ::

    INSTALLED_APPS = [
        ...
        'testtable.apps.TesttableConfig',
        ]


Add a test database table
-------------------------
In shell, ::
    
    python manage.py raisetesttable <db_name>

To see available database tables, run with no database names, ::

    python manage.py raisetesttable


Remove a test database table
----------------------------
In shell, ::

    python manage.py droptesttable <db_name>


Remove completely
--------------------
Drop (see above), then, ::

    python manage.py remove_stale_contenttypes

Then delete the app folder.


Look at the table
-----------------
In a REPL, ::

    $ python manage.py shell
    >>> from testtable.models import Language
    >>> Language.objects.get(pk='eng')

or similar.


The tables
----------
Please note that the data in these tables may be inconsistent and/or inaccurate. The aims are to be useful for db tests, and provide illustration.

Countries
    ISO 3166-1 codes and country names. 254 entries. From https://github.com/umpirsky/country-list
     
Colors
    HTML color names. 864 entries. From https://github.com/codebrainz/color-names

BibleBooks
   Books of the King James Bible, with cross-references to other Bibles (Vulgate, etc.). 80 entries. Constructed from https://en.wikipedia.org/wiki/List_of_books_of_the_King_James_Version
   
Trees
   Tree names. 419 entries. Ony two columns, 'name', 'latin name'. From various UK local government sources.
   
Mineral
    List of minerals with articles on Wikipedia. 1506 entries. Three columns, 'name', 'isvalid', 'reason'. From https://en.wikipedia.org/wiki/List_of_minerals

Languages
    List of three-letter language codes and reference dta. 7850 entries (may take 10 mins to load). Text data with seven columns. DB form and data from www.sil.org/iso639-3/
    
Stars
    Basic details on all visible stars. 87,474 entries (may take hours to load on an SQLite DB) Mix of text and numeric data, with only five columns.  Modified from http://astronexus.com/node/34


Add a new table
----------------

- (Optional) If the data can be sourced online, build a generator to grab the data from a source then, if necessary, convert to csv. Give the file a name which will be unambiguous but terse.

- (if not generated, see above) Get a CSV file and place in the directory '/csv'. Wikipedia is a good source of info - grab data from the 'edit' page, then use regex 'search/replace' to turn into a CSV file.

- Build a model for the CSV data.

- Add the new model to the imports in 'tabledata.py' so 'tabledata' can see it.

- Add an entry to 'tabledata.py' in the 'tabledata' tuple. This has some repetition of the Models, but adds a lot of extra data. The form of the data is usually not important, it should be terse and friendly (or intriuging!). But the filename must be correct, and the fields must match the declarations in the model. 


That's it, done, ::

    python manage.py raisetesttable new_table_name

Possible problems are that the Model fields do not match the CSV file; which can put data in the wrong column. And the fields are not correctly listed in 'tabledata'; which can throw nasty but obvious DB errors. 

Submit a push request. I like new/better tables.
