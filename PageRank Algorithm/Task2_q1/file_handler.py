import os

#create queue and crawled files
def initialise_files(base_url) :
    queue_file='queue.txt'
    crawl_file='crawled.txt'
    directed_graph='directed_graph.txt'
    #corpus_file='corpus.txt'
    if not os.path.isfile(queue_file) :
        write_file(queue_file,base_url)
    if not os.path.isfile(crawl_file):
        write_file(crawl_file,'')
    if not os.path.isfile(directed_graph) :
        write_file(directed_graph,'')

# Editing a file
def write_file(locate,data):
    print "locate is " + locate
    with open(locate,'w') as f:
        f.write(data + '\n')

# Delete the content of file
def delete_file_contents(filename):
    open(filename,'w').close()
    
# Add data onto an existing file.This function would not delete the
# existing data in file.
def append_to_file(filename, data):
    print "append filename is " + filename
    if  os.path.isfile(filename) :
        with open(filename, 'a') as file:
            file.write(data + '\n')

#Convert file to set
def file_set(filename):
    data=set()
    with open(filename, 'r') as f:
        for line in f:
            data.add(line.replace('\n',''))
    return data
    
# Convert set to file
def set_file(links,filename):
    with open(filename,'a') as f:
        for link in links:
            f.write(link+'\n')

#delete the content of set
def delete_crawled_set(set_name):
    set_name.clear()
    
#creating files
#initialise_files('https://en.wikipedia.org/wiki/Sustainable_energy')
'''
def file_queue(filename):
    data=[]
    with open(filename, 'rt') as f:
        for line in f:
            data.append(line.replace('\n',''))
    return data
 '''
def list_file(links,filename):
    delete_file_contents(filename)
    with open(filename,'wt') as f:
        for link in links:
            f.write(link+'\n')
def file_list(filename):
    data=[]
    with open(filename,'rt') as f:
        for link in f:
            data.append(link)
    return data
def file_dict(dic,filename):
    dict_local={}
    with open(filename,'rt') as f:
        for line in f:
            #temp=line.replace('\n',''))
            arr=line.split("/")
            arr1=arr[-1].split("\n")
            dict_local={arr1[0]:""}
            #print dict_local
            dic.update(dict_local)
        return dic
def data_file(data,filename):
    with open(filename,'a') as f:
        f.write(data+'\n')

def file_graphlist(filename):
    data=[]
    with open(filename,'rt') as f:
        for link in f:
            arr=link.split("/")
            arr1=arr[-1].split("\n")
            #print "print data while inialising graphq list" + arr1
            data.append(arr1[0])
        return data
