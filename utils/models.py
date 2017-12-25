from wagtail.wagtailcore.models import Page

class LabPage(Page):
  def get_context(self, request):
    # Update context to include project pages to highlight
    context = super(LabPage, self).get_context(request)
    splashpage = Page.objects.type(SplashPage).first()
    context['top_level_pages'] = splashpage.get_children()
    return context

  class Meta:
    abstract = True


class SplashPage(LabPage):
  class Meta:
    abstract = True

class HighlightPage(LabPage):
  class Meta:
    abstract = True