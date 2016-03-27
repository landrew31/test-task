from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    """docstring for News"""

    class Meta(object):
        verbose_name = 'News'
        verbose_name_plural = 'News'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='News title'
    )

    news_short = models.TextField(
        blank=False,
        null=False,
        default='',
        verbose_name='News short description'
    )

    news_content = models.TextField(
        blank = False,
        verbose_name = 'News text'
    )

    adding_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Posted at'
    )

    def __unicode__(self):
        return '%s' % self.title
