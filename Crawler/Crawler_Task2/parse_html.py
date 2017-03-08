from HTMLParser import HTMLParser
from urlparse import urljoin
from urlparse import urlparse

class Parse_HTML(HTMLParser):
    focused_string=''
    def __init__(self,base_url,focused):
        #super().__init__()
        HTMLParser.__init__(self)
        self.base_url=base_url
        Parse_HTML.focused_string=focused
        #self.page_url=page_url # can exclude page_url from here.
        self.links= set()

    # following method will be called by HTMLParser.feed() function.
    def handle_starttag(self,tag,attrs):
        if tag=='a' :
            for(attribute,value) in attrs:
                if attribute == 'href':
                    if ':' in value:
                        continue                   
                    url=urljoin(self.base_url,value)
                    if not Parse_HTML.focused_string in url:
                        continue                    
                    self.links.add(url)
   # @staticmethod
   # def check_links_data():
   #     for link in soup.find_all('a'):
            
    
    def page_links(self):
        return self.links

    def error(self,message):
        return (str(e))
    
    @staticmethod
    def get_domain_name(url):
        d=urlparse(url)
        domain='%s://%s/wiki'%(d.scheme,d.netloc)
        return domain
  
        
        
