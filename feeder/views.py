# coding: utf-8

import requests
from django.http import HttpResponse

from feeder.xml import enrich_archive_xml


def fetch_archive_xml():
    url = "http://archive.org/services/collection-rss.php?query=creator%3A%22Fanficast%22"
    response = requests.get(url)
    return response.text


def feed(request):
    xml = enrich_archive_xml(fetch_archive_xml())
    return HttpResponse(xml, content_type="text/xml")
