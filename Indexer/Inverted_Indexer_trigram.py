import file_handler
import string
import operator
import time
import collections
import re
#import File_Convertor

index={}
#number_index={}
# a_c_index={}
# d_f_index={}
# g_i_index={}
# j_l_index={}
# m_o_index={}
# p_r_index={}
# s_u_index={}
# v_x_index={}
# y_z_index={}
document_map={}
document_ref_list=[]

trigram_index_table={}
trigram_doc_table={}
trigram_index_tbl_link=[]
filename="URLS.txt"
#filename="URLS_temp.txt"
parsed_Corpus_dir=".\ParsedCorpus\\"
index_file="trigram_index.txt"
trigram_trmfreq_file="trigram_trmfrq_table.txt"
trigram_docfrq_file="trigram_docfrq_table.txt"
doc_ref_file="trigram_doc_ref.txt"
val=0
doc_count=0
doc_list=[]
trigram_doc_tbl_link=[]
x=0
title_exclude=['-','_']
temp_dict={}
try:
    URLList=[]
    URLList=file_handler.load_URL(URLList,filename)
    for url in URLList:
        title=url.split("/")[-1]
        title=''.join(ch for ch in title if ch not in title_exclude)
        file=parsed_Corpus_dir+ title + ".txt"
        x += 1
        doc_id=x
        document_map[title]=doc_id
        temp_dict={}
        trigram_list=[]
        #print temp_dict
        print "Now working on file : " + file + " " + str(doc_id)
        with open(file,'rt') as f:
            for line in f:
                line=line.split("\n")[0]
                chunks=filter(lambda a: a not in ["-", "--"], line.split())
                #for chunk in chunks:
                for i in range(0,len(chunks)-2):
                    trigram_list.append(chunks[i]+ ' '+ chunks[i+1] + ' ' + chunks[i+2])
        print "trigram list created"
        print time.clock()
        # for trigram in trigram_list:
        #     if trigram not in temp_dict:
        #         temp_dict[trigram]=1
        #     else :
        #         temp_dict[trigram]=temp_dict[trigram]+1

        # using counter data structure now
        temp_dict = collections.Counter()
        for trigram in trigram_list:
            temp_dict[trigram] += 1
        #print temp_dict
        print "temp_dict created"
        print time.clock()
        for key in temp_dict:
            if key in index:
                index[key].append((doc_id,temp_dict[key]))
            else:
                index[key]=[(doc_id,temp_dict[key])]
            # if (re.search('\d+', key[:1])):
            #     number_index=file_handler.append_index(number_index,key,doc_id,temp_dict[key])
            # elif(re.search('[a-c]+', key[:1])):
            #     a_c_index=file_handler.append_index(a_c_index,key,doc_id,temp_dict[key])
            # elif (re.search('[d-f]+', key[:1])):
            #     d_f_index=file_handler.append_index(d_f_index,key,doc_id,temp_dict[key])
            # elif (re.search('[g-i]+', key[:1])):
            #     g_i_index=file_handler.append_index(g_i_index,key,doc_id,temp_dict[key])
            # elif (re.search('[j-l]+', key[:1])):
            #     j_l_index=file_handler.append_index(j_l_index,key,doc_id,temp_dict[key])
            # elif (re.search('[m-o]+', key[:1])):
            #     m_o_index=file_handler.append_index(m_o_index,key,doc_id,temp_dict[key])
            # elif (re.search('[p-r]+', key[:1])):1 123 doi
            #     p_r_index=file_handler.append_index(p_r_index,key,doc_id,temp_dict[key])
            # elif (re.search('[s-u]+', key[:1])):
            #     s_u_index=file_handler.append_index(s_u_index,key,doc_id,temp_dict[key])
            # elif (re.search('[v-x]+', key[:1])):
            #     v_x_index=file_handler.append_index(v_x_index,key,doc_id,temp_dict[key])
            # else:
            #     y_z_index=file_handler.append_index(y_z_index,key,doc_id,temp_dict[key])
            #index=file_handler.append_index(index,key,doc_id,temp_dict[key])
        print "index augmented"
        print time.clock()
        #temp_dict = {}
        #print "index for url:" + str(url)

    # index=file_handler.merge_dictionaries(index,number_index)
    # index=file_handler.merge_dictionaries(index,a_c_index)
    # index=file_handler.merge_dictionaries(index,d_f_index)
    # index=file_handler.merge_dictionaries(index,g_i_index)
    # index=file_handler.merge_dictionaries(index,j_l_index)
    # index=file_handler.merge_dictionaries(index,m_o_index)
    # index=file_handler.merge_dictionaries(index,p_r_index)
    # index=file_handler.merge_dictionaries(index,s_u_index)
    # index=file_handler.merge_dictionaries(index,v_x_index)
    # index=file_handler.merge_dictionaries(index,y_z_index)

    print "Dictionaries merged"
    print time.clock()
    print "trigram index has been created in memory.Now going to save in file."
    file_handler.dict_to_file(index,index_file)
    document_ref_list=sorted(document_map.items(), key=operator.itemgetter(1),reverse=False)
    file_handler.indx_table_to_file(document_ref_list,doc_ref_file)

    print "trigram_index is saved."
    print time.clock()

    #doing task 3 for trigrams
    for each_index in index:
        #command to read value of each index
        value = index[each_index]
        # key is the list of dictionary
        for key,val1 in value:
            #print value[key]
            #for k in key:
                #val += key[k]
            val += val1
            doc_count += 1
            doc_list.append(key)
        trigram_index_table[each_index]= val
        doc_list.append(doc_count)
        trigram_doc_table[each_index]=doc_list
        val = 0
        doc_count=0
        doc_list=[]
    bigram_index_tbl_link=sorted(trigram_index_table.items(), key=operator.itemgetter(1),reverse=True)
    bigram_doc_tbl_link=sorted(trigram_doc_table.items(), key=operator.itemgetter(0),reverse=False)
    file_handler.indx_table_to_file(bigram_index_tbl_link,trigram_trmfreq_file)
    file_handler.doc_table_to_file(bigram_doc_tbl_link,trigram_docfrq_file)
    print "trigram_table is saved"
    print time.clock()



except Exception as e:
    print(str(e))






