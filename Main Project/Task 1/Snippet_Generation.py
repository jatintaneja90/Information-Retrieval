
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
#significant_word = []
#print  stop_word_list
for query_id in query_file_dict:
    query = query_file_dict[query_id]
    print 'working on' , query

    bm25_score_list=Query_Processor.process_query_with_relevance(query)
    top_score_doc=[]
    doc_ref_table=BM25.document_map
    i=1
    query_suggest=query
    #fo = open("cacm/common_words.txt", "r+")
    #text = fo.read()

    #print stop_word_list
    # loading top_score_dict using bm25_score_list
    print bm25_score_list
    for key,value in bm25_score_list:
        if i <= 3:
            top_score_doc.append(key)
            i += 1
    # going to generate a snippet
    for doc in top_score_doc:
        print doc, "dcsc"
        temp_dict={}
        temp_list=[]
        words=0
        #doc_snippet_word_list=generateSnippet(doc_ref_table[doc])
        k=0
        significant_word=[]
        with open('../Task 1/ParsedCorpus/'+doc_ref_table[doc]+ '.txt','rt') as f:
            lines=f.readlines()
            sd=len(lines)
            for line in lines:
                line=line.split("\n")[0]
                chunks=line.split()
                for chunk in chunks:
                    if chunk not in stop_word_list and  not (chunk.isdigit()) :  # checking for stop words
                        if chunk not in temp_dict:
                            temp_dict[chunk]=1
                        else :
                            temp_dict[chunk]=temp_dict[chunk]+1
                    #total_term +=1
            for word in temp_dict:
                if word not in stop_word_list:
                    if sd <25:
                        if temp_dict[word]>= (7-.1*(25-sd)):
                            significant_word.append(word)
                    elif sd >=25 and sd <= 40:
                        if temp_dict[word] >= 7:
                            significant_word.append(word)
                    else:
                        if temp_dict[word]>= (7+.1*(sd-40)):
                            significant_word.append(word)

            #temp_list=sorted(temp_dict.items(), key=operator.itemgetter(1),reverse=True)
    print "signi",significant_word



