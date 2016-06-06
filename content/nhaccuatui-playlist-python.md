Title: Lấy link download video playlist nhaccuatui bằng python
Tags: python
Category: Programming
Date: 2016-06-06 12:29 PM

```python
import requests
import lxml.html
import lxml.etree

# playlist link
URL = 'http://www.nhaccuatui.com/video/nong-dan-hien-dai-modern-farmer-tap-1-vietsub-va.THb4WdUW7B5zA.html?listkey=kvvmU18SznJR' 

def get_html(url):
"""
return html text that can be css selected
"""
resp = requests.get(url)
return lxml.html.fromstring(resp.text)

playlist = get_html(URL)

episode_links = [x.attrib['href'] for x in playlist.cssselect('#idScrllVideoInAlbum&gt;li&gt;a')]

xml_links = []

for link in episode_links:
ep = get_html(link)
xml_content = ep.cssselect('meta[itemprop="embedURL"]')[0].attrib['content']
xml_link = xml_content.split("file=")[1]
xml_links.append(xml_link)

for link in xml_links:
xml = lxml.etree.parse(link)
print(xml.xpath('//track/location')[0].text)
```