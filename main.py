from webscrap import WebScrap

project1 = WebScrap('links')

content = project1.scrapPage()

for x in content:
    print x