#import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

#from lxml import etree

def parse_doc(filename):
    # print 1
    # parser=ET.XMLParser(encoding="utf-8")
    # print 2
    fo = open(filename, "r+")
    soup = BeautifulSoup(fo.read(), 'html.parser')
    bodyContent = soup.find("pre")
    text=bodyContent.get_text()
    return text



#testing of function parse_doc
#parse_doc('../temp/CACM-0498.html')
