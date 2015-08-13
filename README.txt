pyton Swiss-system tournament data base scheme implementation.
version 1.0.0 08/11/2015

e-mail:  asintota@gmail.com

This program implements a light Swiss-system tournament data base
scheme, where player information, match score and game pair generation
is managed through a postgres SQL database and the associated Python
DB-API specification. Programe is made off three code modules:
tournament.sql defines required commands for database and associated
tables creation. Created tables are -players- and -matches-. PSQL views
to optain the quantity of played game  and won game by each player are 
defined too. Finally a view to optain players standing information is also
available. 
tournament.py defines a set of function for tournamet management. This
includes a functions for player registration, match report, match player
pairing and player standing as well as some data base access functions.
tournament_test.py defines test functions for tournament.py functionalities.

Execution requirements:

*python 2.7.10 or later

-python download site: https://www.python.org/downloads/
Installation packages for Windows and Mac OS X are available

A deeper explanation about python 2.7.10 Linux installation can be
found here:
http://www.linuxfromscratch.org/blfs/view/svn/general/python2.html

* psycopg2 package
http://initd.org/psycopg/docs/install.html

Execution:
* Uncompress downloaded directory .zip
* On MAC, Windows or Linux open a command line console.
* Go into uncompressed directory and write:
* $:python tournament_test.py