import Queue
from dfs_crawler import DFS_Crawler
from file_handler_dfs import *
from parse_html_dfs import *
import time

HOMEPAGE = 'https://en.wikipedia.org/wiki/Sustainable_energy'
DOMAIN_NAME = Parse_HTML.get_domain_name(HOMEPAGE)
link=set()

def fetcher(seed,search_str):
    depth=1
    linkscount=0
    #cr=Crawler(seed, DOMAIN_NAME)
    while (depth <= 5) and (linkscount <=1000):
        cr.boot()
        print 'Crawled length '+str(len(Crawler.crawled))
        print 'Queue length '+str(len(Crawler.queue))
        print 'Temp length '+str(len(Crawler.temp))
        print 'inside fetcher crawl'
        for link in Crawler.temp.copy():
            if len(Crawler.crawled) >=1000:
                break
            #time.sleep(5) #
            Crawler.crawl_page(link,search_str)
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

def fetch_dfs(seed,d,text):
    print 'inside dfs_fetch'
    if d<6 and len(DFS_Crawler.crawled) <= 1000:
        links=DFS_Crawler.crawl_page(seed,text)
        print 'length of crawled list %s at depth %s' % (len(DFS_Crawler.crawled),d)
        for link in links.copy():
            print link
            if link in DFS_Crawler.crawled:
                continue
        #print link
            fetch_dfs(link,d+1,text)



#res = dfs("https://en.wikipedia.org/wiki/Sustainable_energy")      

######## Start main ######
print 'cr created'
cr=DFS_Crawler(HOMEPAGE)
print ' crawler files initialising'

#initialise_main()
print 'calling fetcher'
#BFS
#fetcher(HOMEPAGE,'solar')       


#DFS
fetch_dfs(HOMEPAGE,1,'solar')
DFS_Crawler.update_files()



    
