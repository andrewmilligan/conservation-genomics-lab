Conservation Genomics Research Institute Website
================================================

This is the Python Django application that runs the Conservation Genomics
Research Institute (CGRI) website. It uses the [Wagtail CMS][1] to manage
content.

## Configuration

After downloading the repository, run `python manage.py configure` from the
root of the repository to configure the application. This will migrate the
database, creating it if needbe, and collect all of the static files into one
location for convenient serving from a web server.



[1]: https://wagtail.io/
