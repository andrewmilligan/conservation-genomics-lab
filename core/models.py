from wagtail.wagtailcore.models import Page


## LabPage
#
#  This abstract class sub-classes the Page class (from Wagtail) and extends it
#  with additional functionality that will be used by all pages on the site,
#  regardless of type.
#
class LabPage(Page):
  def get_context(self, request):
    context = super(LabPage, self).get_context(request)
    splashpage = context['request'].site.root_page
    context['homepage'] = splashpage.specific
    context['top_level_pages'] = splashpage.get_children()
    return context

  class Meta:
    abstract = True


class HighlightPage(LabPage):
  class Meta:
    abstract = True
