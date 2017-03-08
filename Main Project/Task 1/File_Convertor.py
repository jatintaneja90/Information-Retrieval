import file_handler
import string
import time
import os
import HTMLDocParser as HDP
#import re


#filename="temp.txt"
filenumber=0
corpus_dir="../cacm/"
#corpus_dir="../temp/"
parsed_corpus_dir="./ParsedCorpus/"
#parsed_corpus_dir="../temp_parsed/"
try:
    for filename in os.listdir(corpus_dir):
        print filename
        #fo = open(corpus_dir+filename, "r+")
        text = HDP.parse_doc(corpus_dir+filename)
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        # case folding of text
        text=text.lower()
        # removing any non ascii character from text
        parsed_text=''.join([i if ord(i) < 128 else '' for i in text])
        #replace punctuation in text with ' ' excluding numbers like date and Amount
        exclude = set(string.punctuation).difference(set("-"))
        exclude.add('--')
        #checking the first character of text
        str2=""
        if parsed_text[0] in exclude:
            str2 = str2 + " "
        else:
            str2 = str2 + parsed_text[0]
        #checking the whole body content except first and last character
        for ch in range (1,len(parsed_text)-1):
             if parsed_text[ch] in exclude:
                 if parsed_text[ch] in ['/','-',',','.',':'] and parsed_text[ch+1].isdigit() \
                         and parsed_text[ch-1].isdigit():
                     str2 = str2 + parsed_text[ch]
                 else:
                     str2 = str2 + " "
             else:
                 str2 = str2 + parsed_text[ch]
        #checking the last character of text
        if parsed_text[-1] in exclude:
            str2 = str2 + " "
        else:
            str2 = str2 + parsed_text[-1]
    # saving the parsed data into a file
        filename_new=filename.split('.')[0] +".txt"
        file_handler.string_to_file(parsed_corpus_dir+filename_new,str2)
        print "Parsed " + filename + " has been saved"
        print time.clock()
   #
   #      text=''.join([i if ord(i) < 128 else '' for i in str2])
        #print parsed_text
        #parsed_filename=filename.split(".")[-1]
        #response = urlopen(url)
        #html_bytes = response.read()
        #html_string = parsed_text.decode("utf-8")
        #soup = BeautifulSoup(html_string, 'html.parser')
        #title=soup.find("title")        
        #bodyContent = soup.find("div", {"id": "bodyContent"})
        #htmltext=soup.encode("utf-8")
        #text=htmltext.get_text()

        #file_handler.string_to_file(parsed_corpus_dir+filename,text)
        #will do this much
   #      title=''.join(ch for ch in title if ch not in title_exclude) #  remove punctuation from title
   #      #title=title.lower() ## added to apply case folding on title
   #      htmltitle=title
   #      htmlfile=".\Corpus\\" + htmltitle + ".txt"
   #      htmltext=htmltitle + "\n" + htmltext
   #      filenumber += 1
   #      print "saving HTML file : " + htmlfile + " " + str(filenumber)
   #      file_handler.string_to_file(htmlfile,htmltext) # creating html files for first iteration
   #      for http in bodyContent(["script", "style","a"]):
   #          http.extract() # rip http out
   #      text=bodyContent.get_text()
   #
   #  # break into lines and remove leading and trailing space on each
   #      lines = (line.strip() for line in text.splitlines())
   #  # break multi-headlines into a line each
   #      chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
   #  # drop blank lines
   #      text = '\n'.join(chunk for chunk in chunks if chunk)
   #  #text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
   #      text=text.encode("utf-8")
   #      text=title+ "\n" +text
   #      text=text.lower()  # case folding of text
   #      file1=".\ParsedCorpus\\" + title + ".txt"
   # # text=''.join(c for c in text if c not in ["," , "."])
   #      #title=''.join(ch for ch in title if ch not in string.punctuation)
   #
   #      #title=''.join(ch for ch in title if ch not in string.punctuation)
   #      exclude = set(string.punctuation).difference(set("-"))
   #      exclude.add('--')
   #
   #      #exclude=exclude.excode("utf-8")
   #      #text = ''.join(ch for ch in text if ch not in exclude)
   #      #text = ''.join(ch if ch not in exclude else ch.replace(ch,' ') for ch in text)
   #      #text=text.encode("utf-8")
   #      #  replace punctuation in text with ' '
   #      str2=""
   #      if text[0] in exclude:
   #          str2 = str2 + " "
   #      else:
   #          str2 = str2 + text[0]
   #      #str2 = str2 + text[1]
   #      for ch in range (1,len(text)-1):
   #          if text[ch] in exclude:
   #              if text[ch] in ['/','-',',','.'] and text[ch+1].isdigit() and text[ch-1].isdigit():
   #                  str2 = str2 + text[ch]
   #              else:
   #                  str2 = str2 + " "
   #          else:
   #              str2 = str2 + text[ch]
   #      if text[-1] in exclude:
   #          str2 = str2 + " "
   #      else:
   #          str2 = str2 + text[-1]
   #
   #      text=''.join([i if ord(i) < 128 else '' for i in str2])
   #      title=title.lower() ## added to apply case folding on title
   #      #text=title+ "\n" +text
   #      print "saving ParsedHTML file : " + file1 + " " + str(filenumber)
   #      file_handler.string_to_file(file1,text)

except Exception as e:
    print(str(e))
