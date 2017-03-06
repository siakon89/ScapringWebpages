import urllib2
from bs4 import BeautifulSoup
import re
import traceback
import httplib

class WebScrap:

    urls = []

    def __init__(self,linksPath):

        with open(linksPath, 'r') as file:
            WebScrap.urls = file.readlines()

        urlFilter = re.compile(
            r'^(?:http)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        WebScrap.urls = [url.strip() for url in WebScrap.urls if urlFilter.match(url.strip())]


    def scrapPage(self):

        content = []

        for url in WebScrap.urls:

            try:
                hdr = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
                req = urllib2.Request(url, headers=hdr)
                page = urllib2.urlopen(req)
                soup = BeautifulSoup(page.read(), "lxml")

                pageContent = soup.find('div', {'class': 'entry-content'})

                content.append(pageContent.text)

            except urllib2.HTTPError, e:
                print 'HTTPError = ' + str(e.code)
            except urllib2.URLError, e:
                print 'URLError = ' + str(e.reason)
            except httplib.HTTPException, e:
                print 'HTTPException'
            except Exception:
                print 'generic exception: ' + traceback.format_exc()

        return content
