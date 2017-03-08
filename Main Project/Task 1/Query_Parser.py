from bs4 import BeautifulSoup
import collections
import string

def get_all_queries(filename):
    fo = open(filename, "r+")
    soup = BeautifulSoup(fo.read(), 'html.parser')
    bodyContent = soup.find_all('doc')
    query_dict=collections.OrderedDict()
    for k in bodyContent:

        query_id=k.docno.get_text().encode("utf-8").strip()
        query=k.contents[2].encode("utf-8").replace('\n'," ").rstrip().lstrip()
        #changing the case of query
        query=query.lower()
        #removing puntuations from query
        exclude = set(string.punctuation).difference(set("-"))
        exclude.add('--')

        #checking the first character of text
        str2=""
        if query[0] in exclude:
            str2 = str2 + " "
        else:
            str2 = str2 + query[0]
        #checking the whole body content except first and last character
        for ch in range (1,len(query)-1):
             if query[ch] in exclude:
                 if query[ch] in ['/','-',',','.',':'] and query[ch+1].isdigit() \
                         and query[ch-1].isdigit():
                     str2 = str2 + query[ch]
                 else:
                     str2 = str2 + " "
             else:
                 str2 = str2 + query[ch]
        #checking the last character of text
        if query[-1] in exclude:
            str2 = str2 + " "
        else:
            str2 = str2 + query[-1]
        query=str2
        query_dict[query_id]=query
    #print query_dict
    return query_dict

#query_page_loc="../cacm.query"
#get_all_queries(query_page_loc)
