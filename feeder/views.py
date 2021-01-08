# coding: utf-8

from django.http import HttpResponse

from feeder.utils import fetch_archive_xml, enrich_archive_xml


def feed(request):
    xml = enrich_archive_xml(fetch_archive_xml())
    return HttpResponse(xml, content_type='text/xml')
