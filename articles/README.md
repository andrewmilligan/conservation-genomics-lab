Articles
========

The Articles App handles all of the "article" type pages. Conceptually, these
should be pages that have a format similar to an article or blog post. Most
basic pages should most likely be handled by this app.

All of the actual article pages should reside under an `ArticleIndexPage`,
which will display all of its children in an index-type fashion. Each article
page model should subtype the `ArticlePage` abstract class; this enforces that
they can only be children of an `ArticleIndexPage` and gives them an attribute
called `index_entry_template` which the index page relies on to provide a
template to render each article's type-specific index entry.


## Module Structure

* `models`: this is the module that defines the page classes. In the
  [Wagtail][1] framework, most simple changes can be accomplished by simply
  changing the class that defines a page.

* `blocks`: this module defines custom blocks that can be used in stream fields
  to construct flexible pages through the [Wagtail CMS][1].

## Directory Structure

* `templates`: this directory contains all of the HTML templates used to render
  the final pages served at runtime. These are in the [Django Template
  Language][2], which is mostly HTML with additional syntax that can be used to
  insert class- or instance-specific information dynamically.

* `static`: this directory contains all of the static files that are specific
  to the Articles application, including CSS and Javascript files. Django has
  the capability to collect all static files from installed applications into
  one central location for easy serving from a web server like Apache. Read
  more about Django's static file system [here][3].

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
