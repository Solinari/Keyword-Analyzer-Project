#Amazon Search Keyword Analyzer Project

from bs4 import BeautifulSoup
from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

class Collector(HTMLParser):
    '''collector based on the superclass parser'''

    def __init__(self, url):
        
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        '''finds starting tags and appends them if found'''

        if tag == 'a':
            # anchor tells us we are starting at href
            for attr in attrs:
                
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    
                    if absolute[:4] == 'http':
                        self.links.append(absolute)
                        

    def getLinks(self):
        return self.links

# brings the horse all together

url = "http://www.amazon.com/Best-Sellers-Kindle-Store-eBooks/zgbs/digital-text/154606011/ref=zg_bs_nav_kstore_1_kstore"

resource = urlopen(url)

content = resource.read().decode('utf-8', 'ignore')

collector = Collector(url)

collector.feed(content)



def Get_Best_Seller_Links(links):
    '''pull just the links to the best seller categories'''
    
    IsList = "http://www.amazon.com/Best-Sellers-Kindle-Store-"
    BestSellerLists = []

    
    for link in links:
        if IsList in link:

            BestSellerLists.append(link)

    return BestSellerLists




links = Get_Best_Seller_Links(collector.getLinks())

#30 categories
BestSellers = links[46:75]

for sellercat in BestSellers:
    print(sellercat)
print(BestSellers)
counter = 0
for link in links:
    counter += 1
    if link == 'http://www.amazon.com/Best-Sellers-Kindle-Store-Arts-Photography/zgbs/digital-text/154607011':
        print(counter)
        break

#soup = BeautifulSoup(resource.read().decode('utf-8', 'ignore'))

#print(soup)

