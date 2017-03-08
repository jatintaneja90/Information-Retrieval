from file_handler import *

class Dictionary_Creator:
    outlink_dic={}
    inlink_dic={}
    links_data=[]
    pages=[]
    sinklink=[]
    crawled_file=''
    #out_links_data=[]

    #links= file_list(crawled_file)
    #create a dictionary with crawled links.
    #dict = dict.fromkeys(links.split[-1],"")
#for i in range(0,len(Crawler.crawled)):
#    links.append(Crawler.crawled.split[-1])

    #print dict
    # prepare my dictionary according to input queue given.
    def __init__(self):
        #crawled_file="inlink_graph.txt"
        Dictionary_Creator.outlink_dic=graph_dict(Dictionary_Creator.outlink_dic,"inlink_graph.txt")

    #@staticmethod
    def create_linkdata(self):
        #links_data=file_list("inlink_graph.txt")
        #for link in links:
        with open("inlink_graph.txt",'rt') as f:
            for link in f:
                l=link.split("\n",1)
            #arr=l[0].split(" ",1)
                val=l[0].split(" ")[0]
                arr=l[0].split(" ")[1:]
                Dictionary_Creator.inlink_dic[val]=arr

        #print 'inlink dictionary created'
                if len(arr) > 0:
                    #arr=l.split(" ")[1:]
                    for link1 in arr:
                        if link1 in Dictionary_Creator.outlink_dic:
                            Dictionary_Creator.outlink_dic[link1].append(val)
                            #print value
                            #if value == []:
                                #Dictionary_Creator.outlink_dic[link1]=[val]
                            #else:
                                #value.append[val]
                                #Dictionary_Creator.outlink_dic[link1]=value
                #dict_temp={arr[0]:arr[1]}
                #Dictionary_Creator.inlink_dic.update(dict_temp)
                #arr_split=arr[1].split(" ")
                #for i in range(0,len(arr_split)):
                   # key=arr_split[i]
                   # if key in Dictionary_Creator.outlink_dic:
                      #  value=Dictionary_Creator.outlink_dic.get(key,None)
                       # if (arr[0] not in value):
                        #    if value not in "":
                         #       value=value + " " +arr[0]
                         #   else:
                          #      value=value + arr[0]
                           # Dictionary_Creator.outlink_dic[key]=value

            #else:
               # dict_temp={arr[0]:''}
               # Dictionary_Creator.inlink_dic.update(dict_temp)
            #Dictionary_Creator.inlink_dic.update(dict_temp)

            #for i in range(0,len(arr_split)):
                #key=arr_split[i]
                #if key in Dictionary_Creator.outlink_dic:
                    #value=Dictionary_Creator.outlink_dic.get(key,None)
                    #if (arr[0] not in value):
                        #if value not in "":
                            #value=value + " " +arr[0]
                        #else:
                            #value=value + arr[0]
                        #Dictionary_Creator.outlink_dic[key]=value
                        #print "new key value is "+ key +"->" + Dictionary_Creator.outlink_dic.get(key,None)
        print 'inlink dictionary created'
        print Dictionary_Creator.inlink_dic
        print Dictionary_Creator.outlink_dic

    @staticmethod
    def get_pages_set(filename):
        with open("inlink_graph.txt",'rt') as f:
            for link in f:
                l=link.split("\n")
                lnk=l[0].split(" ",1)
                if lnk[0] not in Dictionary_Creator.pages:
                    Dictionary_Creator.pages.append(lnk[0])
        print Dictionary_Creator.pages
        return Dictionary_Creator.pages
    #@staticmethod
    def get_sinklink(self):
        #p=Dictionary_Creator.get_pages_set(Dictionary_Creator.crawled_file)
        p=Dictionary_Creator.get_pages_set("inlink_graph.txt")
        for link in p:
            value=Dictionary_Creator.outlink_dic.get(link,None)
            if len(value) == 0:
             Dictionary_Creator.sinklink.append(link)
        print Dictionary_Creator.sinklink
        #return Dictionary_Creator.sinklink





#dc=Dictionary_Creator()
#dc.create_linkdata()
#dc.get_pages_set(Dictionary_Creator.crawled_file)
#dc.get_sinklink()
