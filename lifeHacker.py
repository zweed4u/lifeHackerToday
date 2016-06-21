import requests
from xml.dom import minidom
session=requests.session()
resp=session.get('http://lifehacker.com/sitemap_today.xml',headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/50.0.2661.102 Chrome/50.0.2661.102 Safari/537.36'})
xmldoc = minidom.parseString(resp.content)
loc_values = xmldoc.getElementsByTagName('loc')
for loc_val in loc_values:
	item=loc_val.firstChild.nodeValue.split('.com')[1].replace('/','').replace('-',' ')[:-11]
	print item.title(),'::',loc_val.firstChild.nodeValue