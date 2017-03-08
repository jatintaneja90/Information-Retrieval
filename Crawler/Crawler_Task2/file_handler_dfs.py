import os

#create queue and crawled files
def initialise_files(base_url) :
    queue_file='queue_dfs.txt'
    crawl_file='crawled_dfs.txt'
    corpus_file='corpus.txt'
    if not os.path.isfile(queue_file) :
        write_file(queue_file,base_url)
    if not os.path.isfile(crawl_file):
        write_file(crawl_file,'')
    if not os.path.isfile(queue_file) :
        write_file(corpus_file,'')

# Editing a file
def write_file(locate,data):
    with open(locate,'w') as f:
        f.write(data)

# Delete the content of file
def delete_file_contents(filename):
    open(filename,'w').close()
    
# Add data onto an existing file.This function would not delete the
# existing data in file.
def append_to_file(filename, data):
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

#handling DFS list seperately
def list_file(l,filename):
    with open(filename,'w') as f:
        for link in l:
            f.write(link+'\n')

    
#creating files
#initialise_files('https://en.wikipedia.org/wiki/Sustainable_energy')
        
    
    
    
    
