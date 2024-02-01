#!/usr/bin/env python
# vim:fileencoding=utf-8
from calibre.web.feeds.news import BasicNewsRecipe

class AdvancedUserRecipe1706826632(BasicNewsRecipe):
    title          = 'El Pais Semanal'
    oldest_article = 8
    max_articles_per_feed = 100
    language       = 'es'
    remove_javascript = True
    remove_empty_feeds = True

    feeds          = [
        ('eps', 'https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/eps'),
    ]