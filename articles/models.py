from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.search import index

from wagtail.core import blocks

from articles.blocks import CaptionedImageBlock, AuthorBlock


## ArticleIndexPage
#
#  This class defines an index for articles. Articles are meant to be housed
#  under an index so that they can all be listed as appropriate. The index's
#  main job is to list all of its children, so it has minimal information of
#  its own.
#
class ArticleIndexPage(Page):
  intro = RichTextField(blank=True)

  content_panels = Page.content_panels + [
      FieldPanel('intro', classname="full")
      ]

  #subpage_types = ['articles.PersonPage', 'articles.ProjectPage']


## ArticlePage
#
#  Abstract base class for all of the article pages. This class enforces that
#  articles will only be created as children of an ArticleIndexPage and that
#  all articles have an `index_entry_template` attribute which is used by the
#  index page to render class-specific index entries.
#
class ArticlePage(Page):
  parent_page_types = ['articles.ArticleIndexPage']
  index_entry_template = 'articles/fragments/default_index_entry.html'

  class Meta:
    abstract = True


## PersonPage
#
#  Article page that defines a person's bio page. Each person has contact
#  information, a position in the lab, a headshot, etc.
#
class PersonPage(ArticlePage):
  email = models.EmailField(blank=True)
  position = models.CharField(max_length=250, blank=True)
  blurb = RichTextField(blank=True)
  bio = RichTextField(blank=True)
  image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.SET_NULL,
      related_name='+',
      null=True
      )

  search_fields = Page.search_fields + [
      index.SearchField('position'),
      index.SearchField('bio'),
      index.SearchField('blurb'),
      ]

  content_panels = Page.content_panels + [
      FieldPanel('email'),
      FieldPanel('position'),
      FieldPanel('bio', classname="full"),
      FieldPanel('blurb', classname="full"),
      ImageChooserPanel('image'),
      ]

  index_entry_template = 'articles/fragments/person_index_entry.html'


## ProjectPage
#
#  Article page the holds a description of a project. Projects can be
#  incredibly varied and likely have associated images, so the body of this
#  class allows a large amount of flexibility in content.
#
class ProjectPage(ArticlePage):
  promoted = models.BooleanField(
      default=False,
      help_text="Promoted pages are highlighted on the home page"
      )
  blurb = RichTextField(blank=True)
  image = models.ForeignKey(
      'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+',
      null=True
      )

  body = StreamField([
      ('heading', blocks.CharBlock(classname="full title", icon='title')),
      ('textblock', blocks.RichTextBlock(label="Text Block")),
      ('image', CaptionedImageBlock()),
      ('pullquote', blocks.BlockQuoteBlock(label="Pull Quote")), 
      ])

  search_fields = Page.search_fields + [
      index.SearchField('blurb'),
      index.SearchField('body'),
      ]

  content_panels = Page.content_panels + [
      FieldPanel('promoted'),
      FieldPanel('blurb', classname="full"),
      ImageChooserPanel('image'),
      StreamFieldPanel('body'),
      ]

  index_entry_template = 'articles/fragments/project_index_entry.html'


## PublicationPage
#
#  Article page the holds a description of a publication. Publications have a
#  lot of specific, structured information.
#
#  TODO: export citation
#
class PublicationPage(ArticlePage):
  author_list = StreamField([('author', AuthorBlock())],
      blank=True)
  date = models.DateField(blank=True, null=True)
  abstract = RichTextField(blank=True, null=True)
  journal = models.CharField(blank=True, null=True, max_length=250)
  pdf = models.ForeignKey(
      'wagtaildocs.Document', null=True, blank=True,
      on_delete=models.SET_NULL, related_name='+'
      )
  link = models.URLField(null=True, blank=True)

  search_fields = Page.search_fields + [
      index.SearchField('author_list'),
      index.SearchField('abstract'),
      index.SearchField('journal'),
      ]

  content_panels = Page.content_panels + [
      StreamFieldPanel('author_list'),
      FieldPanel('date'),
      FieldPanel('abstract', classname="full"),
      FieldPanel('journal'),
      DocumentChooserPanel('pdf'),
      FieldPanel('link'),
      ]

  index_entry_template = 'articles/fragments/publication_index_entry.html'

  citation_template = 'articles/fragments/publication_citation.html'

  def print_author_list(self):
    names = [author.value['name'] for author in self.author_list]
    return ', '.join(names)
