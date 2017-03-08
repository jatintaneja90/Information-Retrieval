from bs4 import BeautifulSoup
import file_handler
from urllib import urlopen
import string
import time
#import re

filename="URLS.txt"
#filename="temp.txt"
filenumber=0
title_exclude=['-','_']

try:
    URLList=[]
    URLList=file_handler.load_URL(URLList,filename)
    for url in URLList:
        title=url.split("/")[-1]
        response = urlopen(url)
        html_bytes = response.read()
        html_string = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html_string, 'html.parser')
        #title=soup.find("title")        
        bodyContent = soup.find("div", {"id": "bodyContent"})
        htmltext=bodyContent.encode("utf-8")
        title=''.join(ch for ch in title if ch not in title_exclude) #  remove punctuation from title
        #title=title.lower() ## added to apply case folding on title
        htmltitle=title
        htmlfile=".\Corpus\\" + htmltitle + ".txt"
        htmltext=htmltitle + "\n" + htmltext
        filenumber += 1
        print "saving HTML file : " + htmlfile + " " + str(filenumber)
        file_handler.string_to_file(htmlfile,htmltext) # creating html files for first iteration
        for http in bodyContent(["script", "style","a"]):
            http.extract() # rip http out
        text=bodyContent.get_text()

    # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
    #text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
        text=text.encode("utf-8")
        text=title+ "\n" +text
        #text=text.lower()  # case folding of text
        file1=".\ParsedCorpus\\" + title + ".txt"
   # text=''.join(c for c in text if c not in ["," , "."])
        #title=''.join(ch for ch in title if ch not in string.punctuation)

        #title=''.join(ch for ch in title if ch not in string.punctuation)
        #exclude = set(string.punctuation).difference(set("-"))
        #exclude.add('--')
        
        #exclude=exclude.excode("utf-8")
        #text = ''.join(ch for ch in text if ch not in exclude)
        #text = ''.join(ch if ch not in exclude else ch.replace(ch,' ') for ch in text)
        #text=text.encode("utf-8")
        #  replace punctuation in text with ' '
        # str2=""
        # if text[0] in exclude:
        #     str2 = str2 + " "
        # else:
        #     str2 = str2 + text[0]
        # #str2 = str2 + text[1]
        # for ch in range (1,len(text)-1):
        #     if text[ch] in exclude:
        #         if text[ch] in ['/','-',',','.'] and text[ch+1].isdigit() and text[ch-1].isdigit():
        #             str2 = str2 + text[ch]
        #         else:
        #             str2 = str2 + " "
        #     else:
        #         str2 = str2 + text[ch]
        # if text[-1] in exclude:
        #     str2 = str2 + " "
        # else:
        #     str2 = str2 + text[-1]

        text=''.join([i if ord(i) < 128 else '' for i in text])
        title=title.lower() ## added to apply case folding on title
        #text=title+ "\n" +text
        print "saving ParsedHTML file : " + file1 + " " + str(filenumber)
        file_handler.string_to_file(file1,text)
        print time.clock()
except Exception as e:
    print(str(e))
