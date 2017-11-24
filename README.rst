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
    List of minerals with articles on Wikipedia. 1506 Entries. Three columns, 'name', 'isvalid', 'reason'. From https://en.wikipedia.org/wiki/List_of_minerals
    
Stars
    Basic details on all visible stars. 87,474 entries (may take hours to load on an SQLite DB) Mix of text and numeric data, with only five columns.  Modified from http://astronexus.com/node/34

Trees is interesting because it is unique on 'latin name' and the 'name' text is complex. BibleBooks is interesting because no column has precidence. Mineral is a longer list, with few columns but an interesting BooleanField.
