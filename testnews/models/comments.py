from __future__ import unicode_literals

from django.db import models

class Comments(models.Model):

    class Meta(object):
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    comment_content = models.TextField(
        blank = False,
        verbose_name = 'News text'
    )

    commented_by = models.CharField(
        max_length=265,
        blank=False,
        verbose_name='Commentator'
    )

    commenting_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Posted at'
    )

    news_commented = models.ForeignKey('News',
        blank=False,
        null=False,
        default=None,
        on_delete=models.PROTECT,
        verbose_name='News Comment'
    )

    def __unicode__(self):
        return '%s at %d %d %d' % (self.commented_by, self.commenting_time.day, self.commenting_time.month, self.commenting_time.year)
