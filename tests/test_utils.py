import re
import os
from xml.etree import ElementTree

import pytest

from feeder.utils import update_items_metadata, enrich_archive_xml, update_channel_metadata


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
    return update_channel_metadata(rss)


def test_update_items_metadata(updated_rss):
    rss = update_items_metadata(updated_rss)
    rss.attrib['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
    xml = ElementTree.tostring(rss).decode()
    assert re.search(r'(\d+).png', xml)


def test_enrich_archive_xml(xml):
    final_xml = enrich_archive_xml(xml).decode()
    open('fanficast.xml', 'w').write(final_xml)
    assert final_xml == """<rss xmlns:ns0="http://search.yahoo.com/mrss/" xmlns:ns1="http://backend.userland.com/creativeCommonsRssModule" version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <link>https://fanficast.com.br/</link>
    <title>Fanficast</title>
    <description>Vem falar de fanfic com a gente! Hospedado por https://archive.org</description>
    <webMaster>contato@fanficast.com.br</webMaster>
    <pubDate>Mon, 21 Aug 2017 03:08:04 GMT</pubDate>
    <image>
      <url>http://fanficast.com.br/static/img/fc_fundo.png</url>
      <title>Fanficast</title>
      <link>https://fanficast.com.br/</link>
    </image>
    <item>
      <title>Fanficando 1 - Game of Thrones</title>
      <ns0:title>Fanficando 1 - Game of Thrones</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=fanficast_fanficando_01_game_of_thrones&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;O Fanficast atravessou o Mar Estreito e chegou em Westeros! Na estreia do &#8220;Fanficando&#8221;, sua j&#225; conhecida host Nana Castro , acompanhada de Talita Souza , da nossa coluna &#8220;Talita Indica&#8221; e Roberta Clemente , do canal "S&#243; Mais Um Epis&#243;dio", far&#227;o fanfics de Game of Thrones, al&#233;m de compar....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/fanficast_fanficando_01_game_of_thrones</link>
      <guid>http://archive.org/details/fanficast_fanficando_01_game_of_thrones</guid>
      <pubDate>Mon, 21 Aug 2017 01:38:46 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc-nd/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/fanficast_fanficando_01_game_of_thrones/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/fanficast_fanficando_01_game_of_thrones/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fanfic, GoT, Game of Thrones, ships, OTP, game of thrones, GoT</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficando 1 - Game of Thrones</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-01.png" /></item>
    <item>
      <title>Fanficast 7 - Mulher Maravilha</title>
      <ns0:title>Fanficast 7 - Mulher Maravilha</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=fanficast_7_mulher_maravilha&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;Direto de Themiscyra (ou quase l&#225;), Ana Rosa Leme e Nana Castro falam do maior e melhor (sim!) filme de super her&#243;i que voc&#234; respeita, Mulher Maravilha! Acompanhadas da convidada Talitha, a Tatah do blog Tatah Blah e de Daniel-san , o &#8220;garoto de programa&#8221; do Fanficast, conversam sobre o quant....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/fanficast_7_mulher_maravilha</link>
      <guid>http://archive.org/details/fanficast_7_mulher_maravilha</guid>
      <pubDate>Sat, 24 Jun 2017 00:49:46 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/fanficast_7_mulher_maravilha/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/fanficast_7_mulher_maravilha/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fanfic, fanfiction, filme, mulher maravilha, steve trevor, ship</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficast 7 - Mulher Maravilha</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-07.png" /></item>
    <item>
      <title>Fanficast 6 - Hist&#243;rias que amamos com finais que odiamos</title>
      <ns0:title>Fanficast 6 - Hist&#243;rias que amamos com finais que odiamos</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=Fanficast6HistoriasQueAmamosComFinaisQueOdiamos&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;Ana Rosa Leme , Nana Castro e Talita sentam para conversar, como nos velhos tempos de faculdade, sobre hist&#243;rias que elas amam, mas que os finais foram &#243;&#8230; Neste epis&#243;dio spoilerento, saiba quando &#233; a hora de abandonar uma s&#233;rie, entenda porque os escritores e roteiritas de franquias (n&#227;o) de....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/Fanficast6HistoriasQueAmamosComFinaisQueOdiamos</link>
      <guid>http://archive.org/details/Fanficast6HistoriasQueAmamosComFinaisQueOdiamos</guid>
      <pubDate>Tue, 30 May 2017 12:12:12 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc-nd/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/Fanficast6HistoriasQueAmamosComFinaisQueOdiamos/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/Fanficast6HistoriasQueAmamosComFinaisQueOdiamos/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fanfic, ficwriter, series, seriado, livros, filmes, finais, hist&#243;rias</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficast 6 - Hist&#243;rias que amamos com finais que odiamos</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-06.png" /></item>
    <item>
      <title>Fanficast 5 - O fandom misterioso de Sherlock</title>
      <ns0:title>Fanficast 5 - O fandom misterioso de Sherlock</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=fanficast_5_o_fandom_misterioso_de_sherlock&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;O jogo come&#231;ou e o endere&#231;o &#233; 221B Baker Street! Neste epis&#243;dio, Ana Rosa Leme e Nana Castro recebem Renata Arruda, Gabriela Troccoli e Daniele Ribeiro, as administradoras da Sherlock Brasil (maior p&#225;gina brasileira sobre Sherlock Holmes no Facebook), para uma conversa descontra&#237;da sobre o mai....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/fanficast_5_o_fandom_misterioso_de_sherlock</link>
      <guid>http://archive.org/details/fanficast_5_o_fandom_misterioso_de_sherlock</guid>
      <pubDate>Sun, 12 Feb 2017 23:44:26 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc-nd/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/fanficast_5_o_fandom_misterioso_de_sherlock/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/fanficast_5_o_fandom_misterioso_de_sherlock/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fanfiction, Sherlock, ship war</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficast 5 - O fandom misterioso de Sherlock</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-05.png" /></item>
    <item>
      <title>Fanficast 4 - O fandom m&#225;gico de Harry Potter</title>
      <ns0:title>Fanficast 4 - O fandom m&#225;gico de Harry Potter</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=fanficast_4_o_fandom_magico_de_harry_potter&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;&#201; n&#243;is que voa, brux&#227;o! Ana Rosa e Nchan mergulham numa conversa cheia de magia! Acompanhadas por Nana Castro, a voz por tr&#225;s do twitter do Fanficast, Renata Ventura , escritora dos livros "A Arma Escarlate" e "A Comiss&#227;o Chapeleira", e Marina Anderi, uma das administradoras do site Potterish, ....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/fanficast_4_o_fandom_magico_de_harry_potter</link>
      <guid>http://archive.org/details/fanficast_4_o_fandom_magico_de_harry_potter</guid>
      <pubDate>Sat, 24 Dec 2016 17:22:31 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc-nd/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/fanficast_4_o_fandom_magico_de_harry_potter/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/fanficast_4_o_fandom_magico_de_harry_potter/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fanfic, fic, ficwriter, podcast</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficast 4 - O fandom m&#225;gico de Harry Potter</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-04.png" /></item>
    <item>
      <title>Fanficast 3 - Yaoi/BL (18+)</title>
      <ns0:title>Fanficast 3 - Yaoi/BL (18+)</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=Fanficast_3_Yaoi_Bl&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;Ana e Nchan batem um papo sobre o BL (Boys Love), mais conhecido por n&#243;s ocidentais como Yaoi. Para isso, o Fanficast contou com a participa&#231;&#227;o da ficwriter Andreia Kennen, escritora desde 2007, amante de Yaoi, tendo produ&#231;&#245;es amplamente ambientadas nos fandons de Naruto e Saint Seya....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/Fanficast_3_Yaoi_Bl</link>
      <guid>http://archive.org/details/Fanficast_3_Yaoi_Bl</guid>
      <pubDate>Sat, 24 Dec 2016 13:48:41 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc-nd/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/Fanficast_3_Yaoi_Bl/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/Fanficast_3_Yaoi_Bl/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fanfic, fic, ficwriter, podcast</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficast 3 - Yaoi/BL (18+)</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-03.png" /></item>
    <item>
      <title>Fanficast 2 - O universo open source de Lovecraft</title>
      <ns0:title>Fanficast 2 - O universo open source de Lovecraft</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=Fanficas_t2_o_universo_open_source_de_lovecraft&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;Ana e Nchan batem um papo com Eduardo Spohr (Filosofia Nerd) sobre um fandom inomin&#225;vel! Neste epis&#243;dio, conhe&#231;a um pouco do universo criado por H.P. Lovecraft e saiba como seu mundo come&#231;ou a ser expandido....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/Fanficas_t2_o_universo_open_source_de_lovecraft</link>
      <guid>http://archive.org/details/Fanficas_t2_o_universo_open_source_de_lovecraft</guid>
      <pubDate>Sat, 24 Dec 2016 12:40:30 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc-nd/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/Fanficas_t2_o_universo_open_source_de_lovecraft/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/Fanficas_t2_o_universo_open_source_de_lovecraft/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fanfic, fic, ficwriter, podcast</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficast 2 - O universo open source de Lovecraft</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-02.png" /></item>
    <item>
      <title>Fanficast 1 - O Abc Das Fanfics</title>
      <ns0:title>Fanficast 1 - O Abc Das Fanfics</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=fanficast_1_o_abc_das_fanfics&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;No epis&#243;dio de hoje n&#243;s apresentamos as palavras que est&#227;o na ponta da l&#237;ngua (e dos dedos) de quem l&#234; e escreve fanfics! Aprenda a classificar uma fanfic a partir de v&#225;rios aspectos, saiba quais s&#227;o as coisas que mais causam disc&#243;rdia entre f&#227;s e conhe&#231;a os tipos de fanfics que mais gosta....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/fanficast_1_o_abc_das_fanfics</link>
      <guid>http://archive.org/details/fanficast_1_o_abc_das_fanfics</guid>
      <pubDate>Sat, 24 Dec 2016 12:09:45 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc-nd/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/fanficast_1_o_abc_das_fanfics/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/fanficast_1_o_abc_das_fanfics/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fic, fanfic, ficwriter, podcast</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficast 1 - O Abc Das Fanfics</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-01.png" /></item>
    <item>
      <title>Fanficast 0 - O que &#233; fanfic</title>
      <ns0:title>Fanficast 0 - O que &#233; fanfic</ns0:title>
      <description>&lt;img width="160" style="padding-right:3px;float:left;" src="http://archive.org/services/get-item-image.php?identifier=fanficast_0_o_que_e_fanfic&amp;mediatype=audio&amp;collection=opensource_audio"/&gt;&lt;p&gt;No epis&#243;dio de estreia do Fanficast, te convidamos para entrar no universo das fanfictions! Entenda o que &#233; um ficwriter, a import&#226;ncia dos leitores para os escritores de fanfics, qual a fun&#231;&#227;o do beta-reader e saiba como conhecemos as fic&#231;&#245;es de f&#227;s! Site: fanficast.com.br/ Facebook: facebo....&lt;/p&gt;&lt;p&gt;This item belongs to: audio/opensource_audio.&lt;/p&gt;&lt;p&gt;This item has files of the following types: Archive BitTorrent, Columbia Peaks, Metadata, Ogg Vorbis, PNG, VBR MP3&lt;/p&gt;</description>
      <link>http://archive.org/details/fanficast_0_o_que_e_fanfic</link>
      <guid>http://archive.org/details/fanficast_0_o_que_e_fanfic</guid>
      <pubDate>Mon, 19 Dec 2016 01:19:04 GMT</pubDate>
      <ns1:license>http://creativecommons.org/licenses/by-nc-nd/3.0/</ns1:license>
      <category>audio/opensource_audio</category>
      <ns0:content url="http://archive.org/download/fanficast_0_o_que_e_fanfic/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" medium="audio" expression="full" isDefault="true" bitrate="128" />
      <enclosure url="http://archive.org/download/fanficast_0_o_que_e_fanfic/format=VBR+MP3&amp;ignore=x.mp3" type="audio/mpeg" length="111111" />
      <ns0:keywords>fanfic, fic, ficwriter, podcast</ns0:keywords>
    <itunes:explicit>false</itunes:explicit><itunes:title>Fanficast 0 - O que &#233; fanfic</itunes:title><itunes:image href="http://fanficast.com.br/static/media/vitrine-quadrada-00.png" /></item>
  <language>pt-br</language><copyright>CC BY-NC-ND 4.0</copyright><itunes:owner><itunes:name>Fanficast</itunes:name><itunes:email>contato@fanficast.com.br</itunes:email></itunes:owner><itunes:author>Fanficast</itunes:author><itunes:summary>Vem falar de fanfic com a gente! Hospedado por https://archive.org</itunes:summary><itunes:type>episodic</itunes:type><itunes:explicit>false</itunes:explicit><itunes:image href="http://fanficast.com.br/static/img/fc_fundo.png" /><itunes:category text="Society & Culture" /><itunes:category text="Arts" /><itunes:category text="Fiction" /></channel>
</rss>"""
