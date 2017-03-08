from urllib import urlopen
from file_handler import *
from parse_html import *
import urlparse
from bs4 import BeautifulSoup
from sets import Set

class Crawler:
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue = set()
    crawled = set()
    temp= set()
    link_value=set()
    finalq=set()
    
    def __init__(self, base_url, domain_name):
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name
        Crawler.queue_file = 'queue.txt'
        Crawler.crawled_file = 'crawled.txt'
       # Crawler.corpus_file = 'corpus.txt'
        initialise_files(Crawler.base_url)
       #self.boot()
       #self.crawl_page(Crawler.base_url)

    # Creates directory and files for project on first run and starts the Crawler
    @staticmethod
    def boot():
        #create_project_dir(Crawler.project_name)
        
        Crawler.temp = file_set(Crawler.queue_file)
        Crawler.crawled = file_set(Crawler.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(url,search):
        if url not in Crawler.crawled:
            Crawler.crawled.add(url)
            for link in Crawler.gather_links(url,search):
                Crawler.queue.add(link)
            
            
            
            

    # #added beautiful soap functionality which is suitable for focused crawling
    @staticmethod
    def gather_links(url,search):
        try:
            response = urlopen(url)
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            soup = BeautifulSoup(html_string, 'html.parser')
            bodyContent = soup.find("div", {"id": "bodyContent"})
            for link in bodyContent.find_all('a'):
                value = str(link.get('href'))
                if ':' in value:
                    continue
                url = urljoin(Crawler.base_url, value)
                if not url.startswith("https://en.wikipedia.org/wiki"):
                    continue
                if '#' in url:
                    continue
                if 'solar' not in url.lower() and 'solar' not in link.text:
                    continue
                Crawler.finalq.add(url)
        except Exception as e:
            print(str(e))
            return set()
        return Crawler.finalq

    
    @staticmethod      
    def add_corpus(url,html):
        append_to_file('corpus.txt',url)
        append_to_file('corpus.txt',html)
    @staticmethod
    def update_files():
        set_file(Crawler.queue, Crawler.queue_file)
        set_file(Crawler.crawled, Crawler.crawled_file)
