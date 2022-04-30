from django.urls import reverse
from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(Sitemap):
    priority = 0.5 
    changefreq = 'weekly' 
    def items(self):
        return [ 'home',]
    def location(self, item):
        return reverse(item)

# 출처: https://enfanthoon.tistory.com/159 [June Dev Blog]