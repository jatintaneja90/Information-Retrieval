import file_handler
import string
import operator
import time
import math
import os
import Query_Parser
from collections import OrderedDict

index={}
unigram_index_table={}
unigram_doc_table={}
doc_score_table={}
unigram_index_tbl_link=[]
filename="URLS.txt"
index_file="unigram_index.txt"
unigram_trmfreq_file="unigram_trmfrq_table.txt"
unigram_docfrq_file="unigram_docfrq_table.txt"
parsed_Corpus_dir=".\ParsedCorpus\\"
doc_ref_file="unigram_doc_ref.txt"
normalised_tf_dict={}
val=0
doc_count=0
doc_list=[]
document_map={}
document_list=[]
unigram_doc_tbl_link=[]
query_file='../cacm.query'
x=0
N=3204
# fik= freq of kth term in ith doc - index
# N =number of docs = 1000
# nk = total freq of kth term -  unigram_doc_table
query_dict={}

query_file_dict=OrderedDict()
#def doc_score(term,doc_id,t):
try:
    for file in os.listdir('../ParsedCorpus'):
        # print 'Test Folder/'+filename
        fo = open('../ParsedCorpus/' + file, "r+")

        temp_dict = {}
        temp_dict1 = {}

        x += 1
        doc_id=x
        document_map[doc_id]=file.split(".")[0]
        document_list.append(doc_id)
        #print " Now working on file : " + file + " " + str(doc_id)

        total_term=0
        for line in fo:
            line=line.split("\n")[0]
            chunks=line.split()
            for chunk in chunks:
                #total_term +=1
                if chunk not in ['-','--']:  ## added  to remove - and -- from final list of terms
                    total_term +=1
                    if chunk not in temp_dict:
                        temp_dict[chunk]=1
                        #total_term +=1
                    else :
                        temp_dict[chunk]=temp_dict[chunk]+1
                        #total_term +=1
        for key in temp_dict:
            temp_dict1[key]=float(temp_dict[key])/total_term
        normalised_tf_dict[doc_id]=temp_dict1
        for key in temp_dict:
            if key in index:
                index[key].update({doc_id:temp_dict1[key]})
            else:
                index[key]={doc_id:temp_dict1[key]}

    #file_handler.dict_to_file(index,index_file)
    document_ref_list=sorted(document_map.items(), key=operator.itemgetter(0),reverse=False)
    file_handler.indx_table_to_file(document_ref_list,doc_ref_file)


    #print normalised_tf_dict[3]
    print "unigram_index is created."
    print time.clock()
    #doing task 3 for unigrams
    for each_index in index:
        #command to read value of each index
        value = index[each_index]
        for key in value:
            #print value[key]
            #val += value[key]
            doc_count += 1
            #doc_list.append(key)
        #unigram_index_table[each_index]= val
        #doc_list.append(doc_count)
        #unigram_doc_table[each_index]=doc_list
        unigram_doc_table[each_index]=doc_count
        #val = 0
        doc_count=0

    unigram_doc_tbl_link=sorted(unigram_doc_table.items(), key=operator.itemgetter(0),reverse=False)
    #file_handler.indx_table_to_file(unigram_index_tbl_link,unigram_trmfreq_file)
    file_handler.doc_table_to_file(unigram_doc_tbl_link,unigram_docfrq_file)
    print "unigram_doc_table is created"
    #print unigram_doc_table
    print time.clock()

    # doc_weight_score=0
    # doc_weight_score_dict={}
    # #for doc in normalised_tf_dict:
    for doc in normalised_tf_dict:
        for term in normalised_tf_dict[doc]:
            idf= 1 + math.log(float(N)/unigram_doc_table[term])
            normalised_tf_dict[doc][term] = normalised_tf_dict[doc][term] * idf
            #doc_weight_score += normalised_tf_dict[doc][term] * normalised_tf_dict[doc][term]
        #doc_weight_score_dict[doc]=doc_weight_score
        #print str(doc) + " | " + str(doc_weight_score)
        #doc_weight_score=0
            #print "Printing normalised_tf_dict"
    print "Printing normalised_tf_dict"
    #print term_weight_doc_dict
    #print normalised_tf_dict[3]
    #print doc_weight_score_dict[1]
    print "normalised_tf_dict is created"
    print time.clock()

    ## processing of query##############################
    query_file_dict= Query_Parser.get_all_queries(query_file)
    print query_file_dict
    for query_id in query_file_dict:
        query=query_file_dict[query_id]
        print "working on query : " + query
        query_temp_dict={}
        total_term=0
        query_weight_score=0
        query_term=query.split()
        # doc_weight_score=0
        # doc_weight_score_dict={}
        # #for doc in normalised_tf_dict:
        # for doc in normalised_tf_dict:
        #     for term in normalised_tf_dict[doc]:
        #         idf= 1 + math.log(float(N)/unigram_doc_table[term])
        #         normalised_tf_dict[doc][term] = normalised_tf_dict[doc][term] * idf
        #         if term in query_term:
        #             doc_weight_score += normalised_tf_dict[doc][term] * normalised_tf_dict[doc][term]
        #     doc_weight_score_dict[doc]=doc_weight_score
        # #print str(doc) + " | " + str(doc_weight_score)
        #     doc_weight_score=0
        # print "Now printing doc_weight_score_dict"
        # print doc_weight_score_dict

        for term in query_term:
            if term not in query_temp_dict:
                query_temp_dict[term] = 1
                total_term += 1
            else:
                query_temp_dict[term]=query_temp_dict[term] + 1
                total_term += 1
        for key in query_temp_dict:
            query_temp_dict[key]=float(query_temp_dict[key])/total_term
        for term in query_temp_dict:
            if term in unigram_doc_table:
                idf=1 + math.log(float(N)/unigram_doc_table[term])
            else:
                idf=0.0
            #idf = 1
        #print str(unigram_doc_table[term])
        #print str(idf) + "for term" + term
            query_temp_dict[term]= query_temp_dict[term] * idf
            query_weight_score += query_temp_dict[term] * query_temp_dict[term]
        print query_temp_dict
        print "query weight score is " + str(query_weight_score)

        doc_weight_score = 0.0
        doc_weight_score_dict = {}
        # for doc in normalised_tf_dict:
        for doc in normalised_tf_dict:
            for term in query_term:
                if term in normalised_tf_dict[doc]:
                    doc_weight_score += normalised_tf_dict[doc][term] * normalised_tf_dict[doc][term]
            doc_weight_score_dict[doc] = doc_weight_score
            # print str(doc) + " | " + str(doc_weight_score)
            doc_weight_score = 0.0
            # print "Printing normalised_tf_dict"
        print "Printing normalised_tf_dict"

        # calculating cosine formula
        num_sum=0.0
        den_sum=0.0
        cosine_score={}
        for doc in normalised_tf_dict:
            for term in query_term:
                if term in normalised_tf_dict[doc]:
                    temp_score=normalised_tf_dict[doc][term] * query_temp_dict[term]
                else:
                    temp_score=0.0
                num_sum += temp_score

            den_sum = math.sqrt(doc_weight_score_dict[doc] * query_weight_score)
            if den_sum == 0:
                cosine_score[document_map[doc]]=0
            else:
                cosine_score[document_map[doc]]=float(num_sum)/den_sum
            #print str(doc) + " | " + str(cosine_score[doc]) + "\n"
            num_sum=0.0
        #print cosine_score
        cosine_score_list=[]
        # sorting on the basis of cosine score
        cosine_score_list=sorted(cosine_score.items(),key=operator.itemgetter(1),reverse=True)
        print "cosine_score_list created"
        file_handler.print_ranked_doc(cosine_score_list,query_id,"Cosine_Similarity_System","../CSquery/Q"+query_id+"cosine_similarity.txt")
except Exception as e:
    print(str(e))



