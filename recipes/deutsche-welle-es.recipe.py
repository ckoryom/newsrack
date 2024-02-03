from calibre.web.feeds.news import BasicNewsRecipe, classes

class DeutscheWelle_es(BasicNewsRecipe):
    title = 'Deutsche Welle'
    __author__ = 'unkn0wn'
    description = 'Noticias desde Alemania y mundo'
    publisher = 'Deutsche Welle'
    language = 'es'

    oldest_article = 1
    max_articles_per_feed = 100
    no_stylesheets = True
    remove_javascript = True
    remove_empty_feeds = True
    ignore_duplicate_articles = {'title', 'url'}

    remove_attributes = ['height', 'width', 'style']

    keep_only_tags = [
        dict(name='article')
    ]
    
    remove_tags = [
        dict(name=['footer', 'source']),
        dict(attrs={'data-tracking-name':'sharing-icons-inline'}),
        classes('kicker advertisement vjs-wrapper')
    ]

    feeds = [
        ('Titulares', 'http://rss.dw-world.de/rdf/rss-sp-top'),
        ('Noticias de Alemania', 'http://rss.dw-world.de/rdf/rss-sp-ale'),
        ('Internacionales', 'http://rss.dw-world.de/rdf/rss-sp-inter'),
        ('Cultura', 'http://rss.dw-world.de/rdf/rss-sp-cul'),
        ('Ciencia y Tecnología', 'http://rss.dw-world.de/rdf/rss-sp-cyt'),
        ('Economía', 'http://rss.dw-world.de/rdf/rss-sp-eco'),
        ('La prensa opina', 'http://rss.dw-world.de/rdf/rss-sp-press'),
        ('Ecología', 'http://rss.dw-world.de/rdf/rss-sp-ecol'),
        ('Futbol alemán', 'http://rss.dw-world.de/rdf/rss-sp-fut'),
        ('Conozca Alemania', 'http://rss.dw-world.de/rdf/rss-sp-con')
    ]

 
    def preprocess_html(self, soup):
        for img in soup.findAll('img', srcset=True):
            img['src'] = img['srcset'].split()[6]
        return soup