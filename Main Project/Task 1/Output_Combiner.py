
source_loc='./Deliverables/Evaluation-output/Pseudo_output_with_Stopping_3w10d/'
destination_loc='./Deliverables/Evaluation-output/Pseudo_output_with_Stopping_3w10d/'
destination_filename="Combined_Evaluation_results.txt"
#source_file="URLS.txt"
i=1
imax=64
combined_text=""
#file_name_dict={}
#file_name_list=[]
while i<=imax:
    filename="Q"+str(i)+"pseudo_rel_result.txt"
    fo = open(source_loc+filename, "r+")
    parsed_text = fo.read()
    combined_text += parsed_text
    combined_text += '\n \n \n \n'
    i += 1
#for filename in os.listdir(source_loc):
    #fil="Q"+i+""
    # fil=filename.split('_')[0]
    # #fil=fil[-1]
    # file_name_dict[fil]=filename

# file_name_list=sorted(file_name_dict.items(), key=operator.itemgetter(0),reverse=False)

# for page_id,page in file_name_list:
#     fo = open(source_loc+page, "r+")
#     parsed_text = fo.read()
#     combined_text += parsed_text
#     combined_text += '\n \n \n \n'
    # filename="Q"+str(i)+"_BM25_score"
    # fo = open(source_loc+filename, "r+")
    # parsed_text = fo.read()
    # combined_text += parsed_text
    # combined_text += '\n \n \n \n'
    # i += 1

with open(destination_loc+destination_filename,'wt') as f:
    f.write(combined_text)


