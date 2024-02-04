#!/usr/bin/env python
# vim:fileencoding=utf-8
from calibre.web.feeds.news import AutomaticNewsRecipe

class InfoQ(AutomaticNewsRecipe):
    title          = 'InfoQ'
    oldest_article = 1
    max_articles_per_feed = 100
    auto_cleanup   = True
    language       = 'en'
    remove_javascript = True
    remove_empty_feeds = True

    feeds          = [
        ('Development', 'https://feed.infoq.com/development/'),
        ('Architecture & Design', 'https://feed.infoq.com/architecture-design/'),
        ('AI, ML & Data Engineering', 'https://feed.infoq.com/ai-ml-data-eng/'),
        ('Culture & Methods', 'https://feed.infoq.com/culture-methods/'),
        ('DevOps', 'https://feed.infoq.com/Devops/'),
    ]