Conservation Genomics Research Institute Website
================================================

This is the Python Django application that runs the Conservation Genomics
Research Institute (CGRI) website. It uses the [Wagtail CMS][1] to manage
content and the lovely [Wagtail Bakery][2] to bake the site to flat HTML for
hosting.


## Configuration

After downloading the repository, run `python manage.py configure` from the
root of the repository to configure the application. This will migrate the
database, creating it if needbe, and collect all of the static files into one
location for convenient serving from a web server.


## Baking to HTML

With the help of [Wagtail Bakery][2], all you have to do is run `python
manage.py build` from the root of the repository to bake the site out to static
HTML. That makes it much easier and lighter to host, improves scalability, and
helps with security too.


[1]: https://wagtail.io/
[2]: https://github.com/wagtail/wagtail-bakery
