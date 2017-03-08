import Query_Processor_with_Stopping
import BM25_With_Stopping
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
#print  stop_word_list
for query_id in query_file_dict:
    query = query_file_dict[query_id]
    print 'working on' ,query

    bm25_score_list=Query_Processor_with_Stopping.process_query_with_relevance(query)
    top_score_doc=[]
    doc_ref_table=BM25_With_Stopping.document_map
    i=1
    query_suggest=query
    #fo = open("cacm/common_words.txt", "r+")
    #text = fo.read()

    #print stop_word_list
    # loading top_score_dict using bm25_score_list
    print bm25_score_list
    for key,value in bm25_score_list:
        if i <= 10:
            top_score_doc.append(key)
            i += 1
    # going to generate a snippet
    for doc in top_score_doc:
        print doc, "dcsc"
        temp_dict={}
        temp_list=[]
        words=0
        #doc_snippet_word_list=generateSnippet(doc_ref_table[doc])

        with open('../Task 1/ParsedCorpus/'+doc_ref_table[doc]+ '.txt','rt') as f:
            print doc_ref_table[doc]
            for line in f:
                line=line.split("\n")[0]
                chunks=line.split()
                for chunk in chunks:
                    if chunk not in stop_word_list:  # checking for stop words
                        if chunk not in temp_dict:
                            temp_dict[chunk]=1
                        else :
                            temp_dict[chunk]=temp_dict[chunk]+1
                    #total_term +=1
            temp_list=sorted(temp_dict.items(), key=operator.itemgetter(1),reverse=True)
            print "hi",temp_list
            for key,value in temp_list:
                if words <= 2:
                    print  key
                    if key not in query_suggest and not(key.isdigit()):
                        query_suggest=query_suggest+" "+key
                        print key
                        words += 1
    print "Expanded query: "+query_suggest
    bm25_score_list = Query_Processor_with_Stopping.process_query_with_relevance(query_suggest)
    print bm25_score_list
    file_handler.print_ranked_doc(bm25_score_list, query_id, "PseudoRelWithStopping_BM25_System",
                                  "../Pseudo_output_with_Stopping_3w10d/Q" + query_id + "pseudo_rel_result.txt")













