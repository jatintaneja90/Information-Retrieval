from urllib import urlopen
from file_handler_dfs import *
from parse_html_dfs import *
import urlparse
from bs4 import BeautifulSoup
from sets import Set

class DFS_Crawler:
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    crawled = set()
    queue = set()
    #temp= set()
    #finalq=set()
    
    def __init__(self,base_url):
        DFS_Crawler.base_url = base_url
        #Crawler.domain_name = domain_name
        #Crawler.queue_file = 'queue.txt'
        DFS_Crawler.crawled_file = 'crawled_dfs.txt'
        #Crawler.corpus_file = 'corpus.txt'
        initialise_files(DFS_Crawler.base_url)
       #self.boot()
       #self.crawl_page(Crawler.base_url)

    @staticmethod
    def crawl_page(url,search):
        if url not in DFS_Crawler.crawled:
            print 'Adding '+url+' to cralwed list'
            DFS_Crawler.crawled.add(url)
            return DFS_Crawler.gather_links(url,search)
            
            

     # #added beautiful soap functionality which is suitable
     #  for focused crawling
    @staticmethod
    def gather_links(url,search):
        DFS_Crawler.queue.clear()
        try:
            response = urlopen(url)
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            soup = BeautifulSoup(html_string, 'html.parser')
            #bodyContent = soup.find("div", {"id": "bodyContent"})
            for link in soup.find_all('a'):
                value = str(link.get('href'))
                if ':' in value:
                    continue
                url = urljoin(DFS_Crawler.base_url, value)
                if not url.startswith("https://en.wikipedia.org/wiki"):
                    continue
                if '#' in url:
                    continue
                if 'solar' not in url.lower() and 'solar' not in link.text:
                    continue
             #   if d>5 :
             #       continue                
                DFS_Crawler.queue.add(url)
        except Exception as e:
            print(str(e))
            return set()
        return DFS_Crawler.queue
    
    @staticmethod      
    def add_corpus(url,html):
        append_to_file('corpus.txt',url)
        append_to_file('corpus.txt',html)
    

    #@staticmethod
    def update_files():
        #set_file(Crawler.queue, Crawler.queue_file)
        dfs_set_file(DFS_Crawler.crawled, DFS_Crawler.crawled_file)
