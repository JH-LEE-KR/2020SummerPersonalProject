from sklearn.feature_extraction.text import CountVectorizer
from split import splitArticles
from konlpy.tag import Okt

list_contents = splitArticles('contents', '\n') # Get contents that '\n' has been removed to compare similarity

okt = Okt()

# Function for determine the type of token being generated
def tokenize(content, pos=["Noun", "Alpha", "Number"]): # Tokenize only nouns, alphabets, and numbers
    return [word 
            for word, tag in okt.pos(content, norm = True, stem = True) # norm -> normalize tokens, stem -> stem tokens
            if len(word) > 1 and tag in pos] # Exclude the single word

count = CountVectorizer(tokenizer=tokenize) 
matrix = count.fit_transform(list_contents).toarray() # Create word tokens from a list of articles and corresponding vectors
row = matrix.shape[0] 
col = matrix.shape[1]

f = open("matrix.txt", 'w', encoding='utf-8') # make matrix
for i in range(0, row):
    for k in range(0, col):
        f.write(str(matrix[i][k]))
        if k != (col - 1): # For delete last ','
            f.write(',') # Split by matrix column
    f.write('\n') # Split by matrix row
f.close()

g = open("voca.txt", 'w', encoding='utf-8') # make voca
voca = list(count.vocabulary_) # A vocabulary created through CountVectorize
voca_list = [0 for i in range(0, col)] # Initialize to zero to modify certain elements of a two-dimensional list
for i in range(0, col):
    index = count.vocabulary_[str(voca[i])] # Words created by count.vocabulary_ are not sorted by index 
    voca_list[index] = voca[i] # -> Find an index for each word and put it in the voca_list as the element of the index
for i in range(0, col):
    g.write(voca_list[i])
    g.write('\n')
g.close()