import file_handler
import string
import operator
import time
#import File_Convertor

index={}
unigram_index_table={}
unigram_doc_table={}
unigram_index_tbl_link=[]
filename="URLS.txt"
index_file="unigram_index.txt"
unigram_trmfreq_file="unigram_trmfrq_table.txt"
unigram_docfrq_file="unigram_docfrq_table.txt"
parsed_Corpus_dir=".\ParsedCorpus\\"
doc_ref_file="unigram_doc_ref.txt"
val=0
doc_count=0
doc_list=[]
document_map={}
unigram_doc_tbl_link=[]
x=0
title_exclude=['-','_']
try:
    URLList=[]
    URLList=file_handler.load_URL(URLList,filename)
    for url in URLList:
        title=url.split("/")[-1]
        title=''.join(ch for ch in title if ch not in title_exclude)
        file=parsed_Corpus_dir+ title + ".txt"
        temp_dict={}
        x += 1
        doc_id=x
        document_map[title]=doc_id
        print " Now working on file : " + file + " " + str(doc_id)
        with open(file,'rt') as f: # reading the parsed file content
            for line in f:
                line=line.split("\n")[0]
                chunks=line.split()
                for chunk in chunks:
                    if chunk not in ['-','--']:  ## added  to remove - and -- from final list of terms
                        if chunk not in temp_dict:
                            temp_dict[chunk]=1
                        else :
                            temp_dict[chunk]=temp_dict[chunk]+1
        for key in temp_dict:
            if key in index:
                index.get(key).update({doc_id:temp_dict[key]})
            else:
                index[key]={doc_id:temp_dict[key]}

    file_handler.dict_to_file(index,index_file)
    document_ref_list=sorted(document_map.items(), key=operator.itemgetter(1),reverse=False)
    file_handler.indx_table_to_file(document_ref_list,doc_ref_file)
    print "unigram_index is saved."
    print time.clock()
    #doing task 3 for unigrams
    for each_index in index:
        #command to read value of each index
        value = index[each_index]
        for key in value:
            #print value[key]
            val += value[key]
            doc_count += 1
            doc_list.append(key)
        unigram_index_table[each_index]= val
        doc_list.append(doc_count)
        unigram_doc_table[each_index]=doc_list
        val = 0
        doc_count=0
        doc_list=[]
    unigram_index_tbl_link=sorted(unigram_index_table.items(), key=operator.itemgetter(1),reverse=True)
    unigram_doc_tbl_link=sorted(unigram_doc_table.items(), key=operator.itemgetter(0),reverse=False)
    file_handler.indx_table_to_file(unigram_index_tbl_link,unigram_trmfreq_file)
    file_handler.doc_table_to_file(unigram_doc_tbl_link,unigram_docfrq_file)
    print "unigram_table is saved"
    print time.clock()



except Exception as e:
    print(str(e))

