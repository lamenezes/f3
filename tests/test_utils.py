import re
import os
from xml.etree import ElementTree

import pytest

from feeder.utils import add_itunes_metadata, edit_archive_xml, update_metadata


RESOURCES_FOLDER = os.path.join(os.path.dirname(__file__), 'resources')


@pytest.fixture
def xml():
    xml_path = os.path.join(RESOURCES_FOLDER, 'fanficast-feed.xml')
    xml_file = open(xml_path)
    return ''.join(xml_file.readlines())


@pytest.fixture
def rss(xml):
    return ElementTree.fromstring(xml)


@pytest.fixture
def updated_rss(rss):
    return update_metadata(rss)


def test_add_itunes_metadata(updated_rss):
    rss = add_itunes_metadata(updated_rss)
    rss.attrib['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
    xml = ElementTree.tostring(rss)
    assert re.search(r'(\d+).png', xml)


def test_edit_archive_xml(xml):
    final_xml = edit_archive_xml(xml)
    assert 'fanficast.com.br/static/img/fc_fundo.png' in final_xml
    assert '1.png' in final_xml
    assert 'https://fanficast.com.br/' in final_xml
    assert 'Podcast brasileiro sobre fanfics' in final_xml
