# function of split title and contents to list
import re
def splitArticles(get, clear = ''): # 
    f = open("output.txt", 'r', encoding='UTF8') # output.txt -> from crawling.py
    list_title = [] # 'empty title list' for make list of every title
    list_contents = [] # 'empty contents list' for make list of every content
    data = f.read()
    split = data.split('>') # Split using '>' at the end of the title and content
    for i in range(0, len(split) - 1): #len(split) - 1 -> To remove the last split blank space
        if clear == '\n': # Remove '\n' and split
            if i%2 == 0:
                list_title.append(re.sub('[\n]', '', split[i])) 
            else:
                list_contents.append(re.sub('[\n]', '', split[i])) 
        else : # Do not remove '\n' and split
            if i%2 == 0:
                list_title.append(split[i].lstrip('\n')) # lstrip('\n') -> for delete for first '\n'
            else:
                list_contents.append(split[i].lstrip('\n')) # lstrip('\n') -> for delete for first '\n'
    f.close()
    if get == 'title':
        return list_title
    elif get == "contents":
        return list_contents
