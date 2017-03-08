import Queue
from crawler import Crawler
from file_handler import *
from parse_html import *
import time

HOMEPAGE = 'https://en.wikipedia.org/wiki/Solar_power'
DOMAIN_NAME = Parse_HTML.get_domain_name(HOMEPAGE)
def fetcher(HOMEPAGE, DOMAIN_NAME):
    depth=1
    linkscount=0
    cr=Crawler(HOMEPAGE, DOMAIN_NAME)
    while (depth <= 5) and (linkscount <=1000):
        cr.boot()
        print 'Crawled length '+str(len(Crawler.crawled))
        print 'Queue length '+str(len(Crawler.queue))
        print 'Temp length '+str(len(Crawler.temp))
        print 'inside fetcher crawl'
        for link in Crawler.temp.copy():
            if len(Crawler.crawled) >=1000:
                break
            #time.sleep(5)
            Crawler.crawl_page(link)
            Crawler.temp.remove(link)
            print link
            print 'Crawled length inside crawl '+str(len(Crawler.crawled))
            print 'Queue length inside crawl '+str(len(Crawler.queue))
            print 'Temp length inside crawl '+str(len(Crawler.temp))
        #print 'done with depth ' + str(depth) 
        linkscount+=len(Crawler.crawled)
        print 'links count at depth ' + str(depth) + 'is '+ str(linkscount)
        print 'length of temp' + str(len(Crawler.temp))
        delete_file_contents(Crawler.queue_file)
        delete_file_contents(Crawler.crawled_file)
        Crawler.update_files()
        print 'files updated'
        delete_crawled_set(Crawler.crawled)
        print 'Crawled length '+str(len(Crawler.crawled))
        delete_crawled_set(Crawler.queue)
        print 'Queue length '+str(len(Crawler.queue))
        delete_crawled_set(Crawler.temp)
        print 'Temp length '+str(len(Crawler.temp))
        print 'sets deleted'
        
        
        #Crawler.temp=Crawler.queue
        #print 'length of temp after assigning is' + str(len(Crawler.temp))
        depth+=1
        

######## Start main ######
print 'cr created'
#cr=Crawler(HOMEPAGE, DOMAIN_NAME)
print ' crawler files initialising'

#initialise_main()
print 'calling fetcher'
fetcher(HOMEPAGE,DOMAIN_NAME)
#Crawler.update_files()
    
