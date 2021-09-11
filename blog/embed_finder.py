# In settings.py use  path of your class in WAGTAILEMBEDS_FINDERS
# WAGTAILEMBEDS_FINDERS = [
#     {
#         'class': 'blog.embed_finder.GistEmbedFinder'
#     }
# ]
# https://docs.wagtail.io/en/stable/advanced_topics/embeds.html?highlight=oembed#custom-embed-finder-classes
# This class extends OEmbedFinder

import json
import re

from datetime import timedelta
from urllib import request as urllib_request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request

from django.utils import timezone

from wagtail.embeds.finders.oembed import OEmbedFinder
from wagtail.embeds.exceptions import EmbedNotFoundException


class GistEmbedFinder(OEmbedFinder):
    def find_embed(self, url, max_width=None, max_height=None):
        endpoint = self._get_endpoint(url)
        if endpoint is None:
            raise EmbedNotFoundException

        # Work out params
        params = self.options.copy()
        params['url'] = url
        params['format'] = 'json'
        if max_width:
            params['maxwidth'] = max_width
        if max_height:
            params['maxheight'] = max_height

        if "gist" in url:
            pattern = "https://gist.github.com/(.*)"
            grp = re.search(pattern, url)
            if grp:
                gist_url = grp.group(1)
                oembed = {
                    "version": "1.0",
                    "type": "rich",
                    "width": 400,
                    "height": 300,
                    "title": "oembed gist",
                    "url": url,
                    "author_name": gist_url,
                    "author_url": "http://github.com/{}".format(gist_url),
                    "provider_name": "Github",
                    "provider_url": "http://www.github.com/",
                    "html": '<script src="https://gist.github.com/{}.js"></script>'.format(gist_url)
                }
            else:
                raise EmbedNotFoundException
        else:
            # Perform request
            request = Request(endpoint + '?' + urlencode(params))
            request.add_header('User-agent', 'Mozilla/5.0')
            try:
                r = urllib_request.urlopen(request)
                oembed = json.loads(r.read().decode('utf-8'))
            except (URLError, json.decoder.JSONDecodeError):
                raise EmbedNotFoundException

        # Convert photos into HTML
        if oembed['type'] == 'photo':
            html = '<img src="%s" alt="">' % (oembed['url'],)
        else:
            html = oembed.get('html')

        # Return embed as a dict
        result = {
            'title': oembed.get('title', ''),
            'author_name': oembed.get('author_name', ''),
            'provider_name': oembed.get('provider_name', ''),
            'type': oembed['type'],
            'thumbnail_url': oembed.get('thumbnail_url'),
            'width': oembed.get('width'),
            'height': oembed.get('height'),
            'html': html,
        }

        try:
            cache_age = int(oembed['cache_age'])
        except (KeyError, TypeError, ValueError):
            pass
        else:
            result['cache_until'] = timezone.now() + timedelta(seconds=cache_age)

        return result
