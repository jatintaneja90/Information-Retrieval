from HTMLParser import HTMLParser
from urlparse import urljoin
from urlparse import urlparse


class Parse_HTML(HTMLParser):

    def __init__(self,base_url,page_url):
        #super().__init__()
        HTMLParser.__init__(self)
        self.base_url=base_url
        self.page_url=page_url # can exclude page_url from here.
        self.links= set()

    # following method will be called by HTMLParser.feed() function.
    def handle_starttag(self,tag,attrs):
        if tag=='a' :
            for(attribute,value) in attrs:
                if attribute == 'href':
                    if ':' in value:
                        continue                   
                    url=urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self,message):
        return (str(e))
    
    @staticmethod
    def get_domain_name(url):
        #d = urlparse(url).scheme(url)+ str(://)+ urlparse(url).netloc
        #d=urlparse(url).netloc
        #d=urlparse(url).geturl()
        d=urlparse(url)
        domain='%s://%s/wiki'%(d.scheme,d.netloc)
        return domain
   # @staticmethod
   # def check_admin_selflink_url(url):
   #     if ('#' in url) or ('admin' in url) or ('Admin' in url):
   #         return true
        
        
