from urllib import urlopen
from file_handler import *
from parse_html import *
import urlparse

class Crawler:
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue = set()
    crawled = set()
    temp= set()
    #finalq=set()
    
    def __init__(self, base_url, domain_name):
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name
        Crawler.queue_file = 'queue.txt'
        Crawler.crawled_file = 'crawled.txt'
        Crawler.corpus_file = 'corpus.txt'
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
    def crawl_page(url):
        if url not in Crawler.crawled:
            Crawler.append_queue(Crawler.gather_links(url))
            #Crawler.temp.remove(url)
            Crawler.crawled.add(url)
            

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(url):
        html_string = ''
        try:
            response = urlopen(url)
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            #Crawler.add_corpus(url,html_string)
            parse = Parse_HTML(Crawler.base_url, url)
            parse.feed(html_string)
        except Exception as e:
            #parse.error(str(e))
            print(str(e))
            return set()
        return parse.page_links()

    # Saves queue data to project files
    @staticmethod
    def append_queue(links):
        for url in links:
            if (url in Crawler.temp) or (url in Crawler.crawled) or (url in Crawler.queue):
                continue
            if not url.startswith('https://en.wikipedia.org/wiki/'):
                continue
            if ('#' in url) or ('admin' in url) or ('Admin' in url):
                continue
            Crawler.queue.add(url)
    @staticmethod      
    def add_corpus(url,html):
        append_to_file('corpus.txt',url)
        append_to_file('corpus.txt',html)
    

    @staticmethod
    def update_files():
        set_file(Crawler.queue, Crawler.queue_file)
        set_file(Crawler.crawled, Crawler.crawled_file)
