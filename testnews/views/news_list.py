from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from ..util import paginate
from ..models import News, Comments

class OneNewsView(TemplateView):
    """docstring for OneNewsView"""

    template_name = 'testnews/show_one_news.html'

    def get_context_data(self, **kwargs):

        context = super(OneNewsView, self).get_context_data(**kwargs)

        queryset = News.objects.get(pk=kwargs['pk'])

        try:
            comments_list = Comments.objects.all().filter(news_commented=queryset)
        except Exception:
            comments_list = []

        context['new'] = ({
            'news': queryset,
            'comments': comments_list,
            })

        return context


class NewsView(TemplateView):

    template_name = 'testnews/news_list.html'

    def get_context_data(self, **kwargs):

        context = super(NewsView, self).get_context_data(**kwargs)

        queryset = News.objects.all().order_by('pk').reverse()

        news = []

        for new in queryset:
            try:
                comments_list = Comments.objects.all().filter(news_commented=new)
            except Exception:
                comments_list = []

            news.append({
                'news': new,
                'comments': len(comments_list),
            })

        context = paginate(news, 3, self.request, context, var_name='news')

        return context
