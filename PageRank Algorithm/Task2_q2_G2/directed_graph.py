from file_handler import *

class Directed_Graph:
    dic={}
    #links=[]

    #links= file_list(crawled_file)
    #create a dictionary with crawled links.
    #dict = dict.fromkeys(links.split[-1],"")
#for i in range(0,len(Crawler.crawled)):
#    links.append(Crawler.crawled.split[-1])

    #print dict
    # prepare my dictionary according to input queue given.
    def __init__(self):
        crawled_file="crawled_final.txt"
        Directed_Graph.dic=file_dict(Directed_Graph.dic,crawled_file)

    #@staticmethod
    def draw(self,link,url):
        #for link in links:
        l=url.split("/")
        url=l[-1]
        arr=link.split("/")
        key=arr[-1]
        if key in Directed_Graph.dic:
            print "inside dict"+key
            value=Directed_Graph.dic.get(key,"")
            if url not in value:
                value=value + " " +url
                Directed_Graph.dic[key]=value
                print "new key value is "+ key +"->" + Directed_Graph.dic.get(key,"")




