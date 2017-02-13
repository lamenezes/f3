# coding: utf-8

import re
import urllib
from xml.etree import ElementTree


def fetch_archive_xml():
    url = 'http://archive.org/services/collection-rss.php?query=creator%3A%22Fanficast%22'
    response = urllib.urlopen(url)
    return ''.join(response.readlines())


def add_itunes_metadata(rss):
    base_image_url = 'http://fanficast.com.br/static/media/vitrine-quadrada-{}.png'
    rss.attrib['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'

    channel = rss.getchildren()[0]
    for item in channel.findall('item'):
        itunes_explicit = ElementTree.SubElement(item, 'itunes:explicit')
        itunes_explicit.text = 'no'

        itunes_author = ElementTree.SubElement(item, 'itunes:author')
        itunes_author.text = 'Fanficast'

        title = item.find('title')
        episode_number = re.match('Fanficast (\d+)', title.text).groups()[0].zfill(2)

        itunes_image = ElementTree.SubElement(item, 'itunes:image')
        itunes_image.attrib['href'] = base_image_url.format(episode_number)

    return rss


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

    rss = add_itunes_metadata(rss)

    return ElementTree.tostring(rss)
