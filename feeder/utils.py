# coding: utf-8

import urllib
from xml.etree import ElementTree


def fetch_archive_xml():
    url = 'http://archive.org/services/collection-rss.php?query=creator%3A%22Fanficast%22'
    response = urllib.urlopen(url)
    return ''.join(response.readlines())


def edit_archive_xml(xml):
    rss = ElementTree.fromstring(xml)
    channel = rss.getchildren()[0]

    link = channel.find('link')
    link.text = u'https://fanficast.com.br/'

    title = channel.find('title')
    title.text = u'Fanficast'

    description = channel.find('description')
    description.text = (u'Podcast brasileiro sobre fanfics, escrita e cultura de fã. '
                        u'Hospedado por https://archive.org')

    webMaster = channel.find('webMaster')
    webMaster.text = u'contato@fanficast.com.br'

    image = channel.find('image')
    image_url = image.find('url')
    image_url.text = u'http://fanficast.com.br/static/img/fc_fundo.png'

    image_title = image.find('title')
    image_title.text = u'Fanficast'

    image_link = image.find('link')
    image_link.text = u'https://fanficast.com.br/'

    return ElementTree.tostring(rss)
