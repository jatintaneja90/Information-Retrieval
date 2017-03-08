from urllib import urlopen
from file_handler import *
from parse_html import *
from bs4 import BeautifulSoup
import urlparse

class Crawler:
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue = []
    crawled = []
    temp= []
    link_number=0
    doc_name = ''
    #finalq=set()
    
    def __init__(self, base_url,domain_name):
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name
        Crawler.queue_file = 'queue.txt'
        Crawler.crawled_file = 'crawled.txt'
        #Crawler.corpus_file = 'corpus.txt'
        initialise_files(Crawler.base_url)
       #self.boot()
       #self.crawl_page(Crawler.base_url)

    # Creates directory and files for project on first run and starts the Crawler

    @staticmethod
    def boot():
        #create_project_dir(Crawler.project_name)
        
        Crawler.temp = Crawler.temp + Crawler.queue
        del Crawler.queue[:]
        list_file(Crawler.crawled,Crawler.crawled_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(url):
        if url not in Crawler.crawled:
            Crawler.gather_links(url)
            #Crawler.temp.remove(url)
            Crawler.crawled.append(url)
           # Crawler.link_number+=1
           # Crawler.doc_name="Doc_" + str(Crawler.link_number)+ ".txt"
            #print "Doc_name is "+ Crawler.doc_name
            #if not os.path.isfile(Crawler.doc_name):


    @staticmethod
    def gather_links(url):
        try:
            response = urlopen(url)
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            soup = BeautifulSoup(html_string,'html.parser')
            #append_to_file(Crawler.doc_name, html_string)
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
                Crawler.queue.append(url)
        except Exception as e:
            print(str(e))
            return []
        Crawler.queue

    @staticmethod
    def add_corpus(url,html):
        append_to_file('corpus.txt',url)
        append_to_file('corpus.txt',html)
    

    @staticmethod
    def update_files():
        #set_file(Crawler.queue, Crawler.queue_file)
        #set_file(Crawler.crawled, Crawler.crawled_file)
        list_file(Crawler.crawled,Crawler.crawled_file)
