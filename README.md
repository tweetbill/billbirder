BillBirder (nee TweetBill)
=========================

BillBirder aims to be a better way to keep track of bills and the politicians who (try to) pass them. Under the hood, it uses data and APIs from the Sunlight Foundation.


Quickstart
----------

Clone this repository (in a `virtualenv`) and install dependencies:

    $ git clone git://github.com/tweetbill/billbirder.git
    $ cd billbirder
    $ pip install -r requirements.txt

Sync your database (there's only one model) and runserver:

    $ python manage.py syncdb
    $ python manage.py runserver
