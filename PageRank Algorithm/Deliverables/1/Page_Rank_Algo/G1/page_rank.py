from file_handler import *
from dictionary_creator import Dictionary_Creator
import math
import operator
import time

def calculate_rank():
    print 'inside calculate rank'
    #for page in Page_Rank.dc.pages:
    ## constant declaration ##
    pr = {}
    newpr = {}
    perplex=[]
    #pr_term = {}
    entropy=0
    page_count = 0
    d = 0.85
    perplexity = 0
    #new_entropy = 0
    new_perplexity = 0
    diff_perplexity = 0
    j = 0
    x = 0
    #getcontext().prec=4
    #perplexity_output_file="G2_perplexity_log.txt"
    #pgrnk_output_file="G2_pg_rnk.txt"
    perplexity_output_file="G1_perplexity_log.txt"
    pgrnk_output_file="G1_pg_rnk.txt"

    #y=0
    ## Instantiate dictionary ##
    dc.create_linkdata()
    dc.get_sinklink()
    page_count=len(dc.pages)

    ## Instantiate probability
    num=1/float(page_count)
    #print 'num = ' + str(num)
    for page in dc.pages:
        pr[page]=num
        #newpr[page]=0
    print 'pr initialised'
    print time.clock()

    while j < 4 :
        x += 1
        sinkPR=0
        new_entropy=0
        entropy=0
        for page in dc.sinklink:
            sinkPR+=pr[page]
        print 'Time after sinkloop' + str(time.clock())
        for page in dc.pages:
            newpr[page] = (1-d)/page_count
            newpr[page] += d*sinkPR/page_count
            #str_in=dc.inlink_dic[page]
            for link in dc.inlink_dic[page]:
                #if link not in dc.sinklink and link in dc.outlink_dic :
                newpr[page]+=d * pr[link]/len(dc.outlink_dic[link])
        print 'Time after new pr loop' + str(time.clock())
        new_entropy=0
        entropy=0
        for page in dc.pages:
            new_entropy += (newpr[page] * math.log(newpr[page],2))
            if x==1:
                entropy += (pr[page] * math.log(pr[page],2))
            pr[page]=newpr[page]
        print 'Time after new entropy loop' + str(time.clock())
        new_entropy = -new_entropy

        if x==1:
            entropy = -entropy
            perplexity=math.pow(2,entropy)
            strng='Value of Perplexity at iteration 0 is ' + str(perplexity)
            print strng
            perplex.append(strng)
        #y+=1
        new_perplexity=math.pow(2,new_entropy)
        diff_perplexity=new_perplexity-perplexity
        #print 'value of perplexity is ' + str(perplexity)
        strng='Value of New Perplexity at iteration ' + str(x) + ' is ' + str(new_perplexity)
        print strng
        perplex.append(strng)
        #print 'value of difference is ' + str(diff_perplexity)
        perplexity=new_perplexity
        #print 'value at loop ' + str(x) + ' is ' + str(diff_perplexity)

        if diff_perplexity < 1:
            j += 1
        else:
            j = 0
        #print 'value of j is' + str (j)
    print 'Saving Perplexity'
    list_file(perplex,perplexity_output_file)
    sorted_pr = sorted(pr.items(), key=operator.itemgetter(1),reverse=True)
    #print pr
    print 'Saving page Rank'
    final_perplex_print(sorted_pr,pgrnk_output_file)



### main ####
dc=Dictionary_Creator()
#print 'initialised Page Rank'
print 'Going to call calculate rank'
calculate_rank()









