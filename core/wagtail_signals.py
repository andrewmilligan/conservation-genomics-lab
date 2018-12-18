from django.core.management import call_command
from wagtail.core.signals import page_published, page_unpublished


def bake_site(sender, **kwargs):
    '''
    This helper function will trigger a re-build of the site automatically when
    a page is published or unpublished so that the static HTML being served
    gets synced with the changes published to the dynamic app.
    '''
    # TODO: either extend this function or call a different command so that we
    #       re-build and also re-deploy here.
    call_command('build')


page_published.connect(bake_site)
page_unpublished.connect(bake_site)
