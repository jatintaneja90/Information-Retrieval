import file_handler
rel_set = {}
file = open("../cacm.rel")
mean_avg_precision =0.0
mean_reciprocal_rank=0.0
prec_at_5={}
prec_at_20={}
avg_prec={}
reciprocal_rank={}


for line in file.readlines():
    key = line.split()[0]
    if key not in rel_set:
        rel_set[key] = [line.split()[2]]
    else:
        rel_set[key].append(line.split()[2])


count=0
sum_avg_prec=0.0
sum_reciprocal_rank=0.0
for i in range(1,65):
    #fo = open("../TASK 1/Q"+str(i)+"cosine_similarity_test.txt", "r+")
    fo = open("../TASK 1/Task1Q" + str(i) + "_tf-idf_score.txt", "r+")
    output=fo.readlines()



    relornonrel_dict={}
    rank = 1
    if str(i) in rel_set:
        for line in output:


            if line.split()[2] in rel_set[str(i)]:
                relornonrel_dict[rank]="R"
            else:
                relornonrel_dict[rank] = "N"
            rank+=1
        print relornonrel_dict

        denom_recall = len(rel_set[str(i)])
        print denom_recall, "Q", i
        num =0
        rank=1
        sum_prec=0.0
        recall={}
        precision={}
        rank_first_rel=0
        for line in output:
            if(relornonrel_dict[rank]) == "R":
                num+=1
                sum_prec+=float(num)/rank
            recall[rank]=float(num)/denom_recall
            precision[rank]=float(num)/rank
            rank+=1

        for rank in relornonrel_dict:
            if relornonrel_dict[rank] =="R":
                rank_first_rel=rank
                break

        reciprocal_rank=float(1)/rank_first_rel
        avg_prec=sum_prec/float(num)
        sum_avg_prec+=avg_prec
        sum_reciprocal_rank+=reciprocal_rank
        prec_at_5[i]=precision[5]
        prec_at_20[i]=precision[20]
        count+=1
        print recall
        print precision
mean_avg_precision=float(sum_avg_prec)/count
mean_reciprocal_rank=float(reciprocal_rank)/count
print mean_reciprocal_rank,"sjxjax", mean_avg_precision
