from bs4 import BeautifulSoup
import collections
import string


def get_all_queries(filename):
    fo = open(filename, "r+")
    soup = BeautifulSoup(fo.read(), 'html.parser')
    bodyContent = soup.find_all('doc')
    query_dict=collections.OrderedDict()
    stop_word_file ='../common_words'
    fo = open(stop_word_file, "r+")
    stop_words = fo.read().splitlines()
    #removing puntuations from query
    exclude = set(string.punctuation).difference(set("-"))
    exclude.add('--')
    #exclude_stoppers=()
    # for word in stop_words:
    #     exclude_stoppers.add(word) # doing stopping now in query
    for k in bodyContent:

        query_id=k.docno.get_text().encode("utf-8").strip()
        query=k.contents[2].encode("utf-8").replace('\n'," ").rstrip().lstrip()
        #changing the case of query
        query=query.lower()

        #checking the first character of text
        str2=""
        print "working on query" + query
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
        # now removing  stop words from query
        query_words=query.split()
        s=""
        for words in query_words:
            if words not in stop_words:
                s += words+" "

        query_dict[query_id]=s.rstrip()
    #print query_dict
    return query_dict

#query_page_loc="../cacm.query"
#get_all_queries(query_page_loc)
