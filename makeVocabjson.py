from eunjeon import Mecab
import json
from collections import OrderedDict
import re

token = Mecab()

with open("output.txt", 'r', encoding='utf-8') as f: # output.txt -> from crawling.py
    document = f.read()

list_morphs = token.morphs(document)

for k in range(0, len(list_morphs)):
    list_morphs[k] = re.sub('[^a-zA-Zㄱ-ㅎㅏ-ㅣ가-힣]', '', list_morphs[k]) # Delete everything except English and Korean.

# Using the characteristics of the set to remove duplication.
list_clear = set(list_morphs)
list_clear = list(list_clear)

data = OrderedDict()

index = 1 # To index vocabulary
for i in range(0, len(list_clear)):
    if list_clear[i].strip() == '': # Remove 'null-element' that is created during conversion from set to list.
        continue
    else:
        data[index] = list_clear[i].strip()
        index += 1
with open("vocab.json", 'w', encoding='utf-8') as jsonfile: 
    json.dump(data, jsonfile, ensure_ascii=False, indent='\t')
