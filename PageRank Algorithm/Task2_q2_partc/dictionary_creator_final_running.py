from file_handler import *
import time


class Dictionary_Creator:
    outlink_dic={}
    inlink_dic={}
    links_data=[]
    pages=[]
    sinklink=[]
    #crawled_file=''
    inlink_file_to_read="G2.txt"
    #inlink_file_to_read="inlink_graph.txt"

    def __init__(self):
        pass
        #crawled_file="inlink_graph.txt"
        #Dictionary_Creator.outlink_dic=graph_dict(Dictionary_Creator.outlink_dic,self.inlink_file_to_read)

    #@staticmethod
    def create_linkdata(self):
        with open(self.inlink_file_to_read,'rt') as f:
            for link in f:
                l=link.split('\n',1)
                val=l[0].split(" ")[0]
                arr=l[0].split(" ")[1:]
                Dictionary_Creator.inlink_dic[val]=arr
                Dictionary_Creator.outlink_dic[val]=[]
        #print 'inlink dic'
        #print Dictionary_Creator.inlink_dic

        for key in Dictionary_Creator.inlink_dic:
            value=Dictionary_Creator.inlink_dic[key]
            if len(value) > 0:
                    for link1 in value:
                        #if link1 in Dictionary_Creator.outlink_dic:
                        Dictionary_Creator.outlink_dic[link1].append(key)
        #print 'outlink dic'
        #print Dictionary_Creator.outlink_dic
        print 'inlink dictionary created' + str(time.clock())


    @staticmethod
    def get_pages_set(filename):
        Dictionary_Creator.pages=Dictionary_Creator.inlink_dic.keys()
        #print Dictionary_Creator.pages
        print 'pages created' + str(time.clock())
        return Dictionary_Creator.pages
    #@staticmethod
    def get_sinklink(self):
        p=Dictionary_Creator.get_pages_set(self.inlink_file_to_read)
        for link in p:
            value=Dictionary_Creator.outlink_dic.get(link,None)
            if len(value) == 0:
             Dictionary_Creator.sinklink.append(link)
        print 'sinklink created' + str(time.clock())
        #print Dictionary_Creator.sinklink
        #return Dictionary_Creator.sinklink





#dc=Dictionary_Creator()
#dc.create_linkdata()
#dc.get_pages_set(Dictionary_Creator.crawled_file)
#dc.get_sinklink()
