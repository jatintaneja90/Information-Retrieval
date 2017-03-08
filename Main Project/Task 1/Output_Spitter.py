
source_loc='./Deliverables/Task 1/lucene/'
source_file='Lucene_Results.txt'
destination_loc='./Deliverables/Task 1/lucene/'
temp_dict={}
fo = open(source_loc+source_file, "r+")
parsed_text = fo.read()
# i=1
# j=100
for line in parsed_text:
    if "query" in line:
        l=line.split()
        l[0]
        if l[0] in temp_dict:
            temp_dict[[0]]=temp_dict[[0]] + "\n"+line
        else:
            temp_dict[l[0]]=line
print temp_dict
for i in temp_dict:
    filename=i+"_lucene.txt"
    with open(destination_loc+filename,'wt') as f:
        f.write(temp_dict[i])







