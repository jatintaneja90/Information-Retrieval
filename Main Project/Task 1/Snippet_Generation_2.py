import Query_Processor
import BM25
import operator
import time
import file_handler
import Query_Parser

print "starting psuedo relevance feedback model"
print time.clock()
query_file='../cacm.query'
query_file_dict = Query_Parser.get_all_queries(query_file)
fo = open('..'+'\common_words', "r+")
stop_word_list = fo.read().splitlines()
for query_id in query_file_dict:
    query = query_file_dict[query_id]
    print 'working on' , query
    bm25_score_list=Query_Processor.process_query_with_relevance(query)
    top_score_doc=[]
    doc_ref_table=BM25.document_map
    i=1
    query_suggest=query
    # loading top_score_dict using bm25_score_list
    print bm25_score_list
    for key,value in bm25_score_list:
        if i <= 3:
            top_score_doc.append(key)
            i += 1
    for doc in top_score_doc:
        with open('../Task 1/ParsedCorpus/'+doc_ref_table[doc]+ '.txt','rt') as f:
            for line in f:
                l=line.split()
                for j in l:
                    if j in query:

