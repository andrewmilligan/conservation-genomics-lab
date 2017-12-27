Core
====

The Core App wraps up some basic functionality that is fundamental to the
project as a whole. Most notably, it provides some abstract base classes that
can be sub-typed by the site pages to inherit functionality that is common to
all of them. It also provides some project-level admin commands that are not
specific to any app in particular.


## Module Structure

* `models`: this is the module that defines the page classes. The Core
  application is not intended to provide any concrete page classes, so none of
  these pages should actually be created. They simply serve as abstract base
  classes to make common functionality easily accessible.


## Directory Structure

* `templates`: this directory contains all of the HTML templates used to render
  the final pages served at runtime. These are in the [Django Template
  Language][1], which is mostly HTML with additional syntax that can be used to
  insert class- or instance-specific information dynamically. In the Core app,
  these should be parent templates that are extended in other applications.

* `static`: this directory contains all of the static files that are specific
  to the Home application, including CSS and Javascript files. Django has the
  capability to collect all static files from installed applications into one
  central location for easy serving from a web server like Apache. Read more
  about Django's static file system [here][2]. In the Core app, these should be
  static resources that are common to the entire site.


TODO: find these URLs
[1]: Django Template Language
[2]: Django static files
