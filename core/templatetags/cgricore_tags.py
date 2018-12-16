from django import template


register = template.Library()


@register.inclusion_tag("core/navbar.html", takes_context=True)
def cgri_navbar(context, fixed=True, light=True):
    '''
    This template tag is used to produce the navigation bar at the top of all
    of the CGRI lab pages. It automatically pulls in the home page and the
    index pages that are the homepage's immediate children to place them in the
    navbar.
    '''
    splashpage = context['request'].site.root_page.specific
    top_level_pages = splashpage.get_children()
    return {
            'homepage': splashpage,
            'top_level_pages': top_level_pages,
            'fixed': fixed,
            'light': light,
            }


@register.inclusion_tag("core/footer.html", takes_context=True)
def cgri_footer(context):
    '''
    This template tag is used to create the CGRI navigation footer that appears
    on all of the lab pages. It uses a similar logic to the navbar to pull in
    the index pages that will show up.
    '''
    splashpage = context['request'].site.root_page.specific
    top_level_pages = splashpage.get_children()
    return {
            'homepage': splashpage,
            'top_level_pages': top_level_pages,
            }
