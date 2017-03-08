from file_handler import *
from dictionary_creator import Dictionary_Creator
import math
import decimal



def calculate_rank():
    print 'inside calculate rank'
    #for page in Page_Rank.dc.pages:
    ## constant declaration ##
    pr = {}
    newpr = {}
    #pr_term = {}
    entropy=0
    page_count = 0
    d = 0.85
    perplexity = 0
    new_entropy = 0
    new_perplexity = 0
    diff_perplexity = 0
    j = 0
    x = 0
    ## Instantiate dictionary ##
    dc.create_linkdata()
    dc.get_sinklink()
    page_count=len(dc.pages)

    ## Instantiate probability
    num=1/float(page_count)
    print 'num = ' + str(num)
    for page in dc.pages:
        pr[page]=num
        #newpr[page]=0
    print pr
    #for page in dc.pages:
        #entropy += (pr[page] * math.log(pr[page],2))
    #entropy = -entropy
    #perplexity=pow(2,entropy)
    #print 'initial perplexity is ' + str(perplexity)
    ## while loop to calculate perplexity
    while j < 4 :
        x += 1
        sinkPR=0
        for page in dc.sinklink:
            sinkPR+=pr[page]
        for page in dc.pages:
            newpr[page]=(1-d)/page_count
            newpr[page]+=d*sinkPR/page_count
            print newpr
            str_in=dc.inlink_dic.get(page,None)
            print 'inlink of page' + page + 'is'
            print str_in
            if len(str_in) > 0:
                #str_in_list=str_in.split(" ")
                for link in str_in:
                    #pg=str_in_list[i]
                    pr_value=pr.get(link,None)
                    str_out=dc.outlink_dic.get(link,None)
                    if len(str_out) > 0:
                        #str_out_list=str_out.split(" ")
                        #str_out_len=len(str_out_list)
                        newpr[page]+=(d * pr_value)/len(str_out)
        print 'pr is'
        print pr
        print 'new pr is'
        print newpr
        for page in dc.pages:
            new_entropy += (newpr[page] * math.log(newpr[page],2))
        new_entropy = -new_entropy
        for page in dc.pages:
            entropy += (pr[page] * math.log(pr[page],2))
        entropy = -entropy
        for page in dc.pages:
            pr[page]=newpr[page]
        print pr
        #for page in dc.pages:
            #new_entropy += (pr[page] * math.log(pr[page],2))
        #new_entropy = -new_entropy
        print 'entropy is '+ str(entropy)
        print 'new_entropy is '+ str(new_entropy)
        perplexity=math.pow(2,entropy)
        new_perplexity=math.pow(2,new_entropy)
        diff_perplexity=new_perplexity-perplexity
        print 'value of perplexity is ' + str(perplexity)
        print 'value of new_perplexity is ' + str(new_perplexity)
        #print 'value of difference is ' + str(diff_perplexity)
        #perplexity=new_perplexity
        print 'value at loop ' + str(x) + ' is ' + str(diff_perplexity)

        if diff_perplexity < 1 :
            j += 1
        else:
            j = 0
        print 'value of j is' + str (j)
    print pr



### main ####
dc=Dictionary_Creator()
#print 'initialised Page Rank'
print 'Going to call calculate rank'
calculate_rank()









