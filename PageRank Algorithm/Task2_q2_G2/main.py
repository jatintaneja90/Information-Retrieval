import Queue
from crawler import Crawler
from file_handler import *
from parse_html import *
import time

HOMEPAGE = 'https://en.wikipedia.org/wiki/Sustainable_energy'
DOMAIN_NAME = Parse_HTML.get_domain_name(HOMEPAGE)
#depth = 1
#linkscount=0
#prs = Parse_HTML(HOMEPAGE,DOMAIN_NAME)
#queue = Queue()
#QUEUE_FILE = 'queue.txt'
#CRAWLED_FILE = 'crawled.txt'


#initialising crawler 


# depth 1 crawling
#cr.crawl_page(HOMEPAGE)

#Crawler.update_files()

#def initialise_main():
#    depth = 1
#    linkscount=0

    # QUEUE_FILE = 'queue.txt'
   # CRAWLED_FILE = 'crawled.txt'



#m=1
def fetcher():
    depth=1
    Crawler.temp.append(HOMEPAGE)
    #linkscount=0
    while depth <= 5 :
        cr.boot()
        print 'Crawled length '+str(len(Crawler.crawled))
        print 'Queue length '+str(len(Crawler.queue))
        print 'Temp length '+str(len(Crawler.temp))
        print 'inside fetcher crawl'
        for link in Crawler.temp:
            if len(Crawler.crawled) >= 1000:
                break
            #time.sleep(5)
            print Crawler.temp[0]
            Crawler.crawl_page(Crawler.temp[0])
            Crawler.temp.pop(0)
           #0 print link
            print 'Crawled length inside crawl at depth '+ str(depth) + ' is ' + str(len(Crawler.crawled))
            print 'Queue length inside crawl at depth '+ str(depth) + ' is '+ str(len(Crawler.queue))
            print 'Temp length inside crawl at depth '+ str(depth) + ' is '+ str(len(Crawler.temp))
        #print 'done with depth ' + str(depth) 
        #linkscount+=len(Crawler.crawled)
        #print 'links count at depth ' + str(depth) + 'is '+ str(linkscount)
        print 'length of temp' + str(len(Crawler.temp))
        #delete_file_contents(Crawler.queue_file)
        #delete_file_contents(Crawler.crawled_file)
        #Crawler.update_files()
        #print 'files updated'
        #delete_crawled_set(Crawler.crawled)
        #print 'Crawled length '+str(len(Crawler.crawled))
        #delete_crawled_set(Crawler.queue)
        #print 'Queue length '+str(len(Crawler.queue))
        #delete_crawled_set(Crawler.temp)
        #print 'Temp length '+str(len(Crawler.temp))
        #print 'sets deleted'
        
        #Crawler.temp=Crawler.queue
        #print 'length of temp after assigning is' + str(len(Crawler.temp))
        depth += 1
        
#def




######## Start main ######
print 'cr created'
cr=Crawler(HOMEPAGE, DOMAIN_NAME)
print ' crawler files initialising'

#initialise_main()
print 'calling fetcher'
fetcher()       
#Crawler.update_files()
cr.save_graph()
