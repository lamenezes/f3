# coding: utf-8

import re
from xml.etree import ElementTree


def enrich_archive_xml(xml):
    rss = parse_xml(xml)
    rss = update_channel_metadata(rss)
    rss = update_items_metadata(rss)
    return ElementTree.tostring(rss)


def parse_xml(xml):
    return ElementTree.fromstring(xml)


def update_channel_metadata(rss):
    channel = list(rss)[0]
    fanficast_logo_url = "http://fanficast.com.br/static/img/fc_fundo.png"
    description = "Vem falar de fanfic com a gente! Hospedado por https://archive.org"
    fields = {
        "link": "https://fanficast.com.br/",
        "language": "pt-br",
        "title": "Fanficast",
        "description": description,
        "webMaster": "contato@fanficast.com.br (Fanficast)",
        "image": {
            "url": fanficast_logo_url,
            "title": "Fanficast",
            "link": "https://fanficast.com.br/",
        },
        "copyright": "CC BY-NC-ND 4.0",
        "itunes:owner": {
            "itunes:name": "Fanficast",
            "itunes:email": "contato@fanficast.com.br",
        },
        "itunes:author": "Fanficast",
        "itunes:summary": description,
        "itunes:type": "episodic",
        "itunes:explicit": "no",
    }
    _append_or_update_fields(channel, fields, position=6)

    channel.insert(6, ElementTree.Element("itunes:image", attrib={"href": fanficast_logo_url}))
    channel.insert(6, ElementTree.Element("itunes:category", attrib={"text": "Society & Culture"}))
    channel.insert(6, ElementTree.Element("itunes:category", attrib={"text": "Arts"}))
    channel.insert(6, ElementTree.Element("itunes:category", attrib={"text": "Fiction"}))

    attribs = {
        "href": "https://feed.fanficast.com.br/",
        "rel": "self",
        "type": "application/rss+xml",
    }
    channel.insert(6, ElementTree.Element("atom:link", attrib=attribs))

    return rss


def _append_or_update_fields(node, fields: dict, position=-1):
    for field_name, value in fields.items():
        field = node.find(field_name)
        if field is None:
            field = ElementTree.Element(field_name)
            node.insert(position, field)

        if isinstance(value, dict):
            _append_or_update_fields(field, value)
            continue

        field.text = value


def update_items_metadata(rss):
    rss.attrib["xmlns:itunes"] = "http://www.itunes.com/dtds/podcast-1.0.dtd"
    rss.attrib["xmlns:atom"] = "http://www.w3.org/2005/Atom"

    channel = list(rss)[0]
    for item in channel.findall("item"):
        fields = {
            "itunes:explicit": "no",
            "itunes:title": item.find("title").text,
        }
        _append_or_update_fields(item, fields)

        itunes_image = ElementTree.SubElement(item, "itunes:image")
        itunes_image.attrib["href"] = _get_image_url(item)

    return rss


def _get_image_url(item):
    # TODO: change podcast image name convention to:
    # vitrine-quadrada-fanficando-1 or vitrine-quadrada-fanficast-2 or
    # vitrine-quadrada-virilhada-cultural-10

    title = item.find("title")
    base_image_url = "http://fanficast.com.br/static/media/vitrine-quadrada-{}.png"
    episode_number = re.match(r".* (\d+) - .*", title.text).groups()[0]
    return base_image_url.format(episode_number.zfill(2))
