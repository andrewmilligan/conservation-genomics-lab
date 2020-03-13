Home
====

The Home App handles the main splash page of the website.


## Module Structure

* `models`: this is the module that defines the page classes. In the
  [Wagtail][1] framework, most simple changes can be accomplished by simply
  changing the class that defines a page.


## Directory Structure

* `templates`: this directory contains all of the HTML templates used to render
  the final pages served at runtime. These are in the [Django Template
  Language][2], which is mostly HTML with additional syntax that can be used to
  insert class- or instance-specific information dynamically.

* `static`: this directory contains all of the static files that are specific
  to the Home application, including CSS and Javascript files. Django has the
  capability to collect all static files from installed applications into one
  central location for easy serving from a web server like Apache. Read more
  about Django's static file system [here][3].

* `migrations`: Django keeps track of the database structure that corresponds
  to the class structure in an application in order to programmatically set up
  the right database and update in-use databases without losing data. The steps
  to accomplish this are stored in the `migrations` directory. Read more about
  the Django migration system [here][4].


TODO: find these URLs
[1]: wagtail
[2]: Django Template Language
[3]: Django static files
[4]: Django migration system
