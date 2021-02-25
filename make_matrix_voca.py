from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Kkma
from readCsv import getTitles, getContents

print('기사정보 불러오기 시작')
list_titles = getTitles()
list_contents = getContents()
print('기사 정보 불러왔음')

kkma = Kkma()

# 토큰화된 단어의 타입을 결정해준다
def tokenize(content): 
    list_result = []
    tags=["NNG", "NNP", "NNB", "NNM", "NR", "NP", "OL", "ON"] # NNG : 보통명사, NNP : 고유 명사, NNB : 일반 의존 명사 , NNM : 단위 의존 명사, NR : 수사, NP : 대명사, OL : 외국어, ON : 숫자
    for word, tag in kkma.pos(content):
        if len(word) > 1 and tag in tags: # tags의 품사에 해당되지 않거나 한 글자 짜리는 넣지 않는다.
            list_result.append(word)
    return list_result

print('토큰화 시작')
count = CountVectorizer(tokenizer=tokenize) 
matrix = count.fit_transform(list_contents).toarray() # tokenize를 이용한 토큰화된 단어와 뉴스 기사간의 행렬
row = matrix.shape[0]
col = matrix.shape[1]

print(row)
print('그리고')
print(col)

print('matrixInfo.txt 파일 생성중...')
with open('matrixInfo.txt','w') as f:
  f.write(str(row))
  f.write('\n')
  f.write(str(col))
print('matrixInfo.txt 파일 생성완료.')

print('matrix.txt 파일 생성중...')
f = open("matrix.txt", 'w', encoding='utf-8') 
for i in range(0, row):
    for k in range(0, col):
        f.write(str(matrix[i][k]))
        if k != (col - 1): 
            f.write(',') # 열 단위로 분리
    f.write('\n') # 행 단위로 분리
f.close()
print('matrix.txt 파일 생성완료.')

print('voca.txt 파일 생성중....')
g = open("voca.txt", 'w', encoding='utf-8') 
voca = list(count.vocabulary_) 
voca_list = [0 for i in range(0, col)] 
for i in range(0, col):
    index = count.vocabulary_[str(voca[i])] # CountVectorizer에 의해 생성된 단어장. 단, 실제 단어의 인덱스의 순서로 구성되어 있는 것은 아니다.
    voca_list[index] = voca[i] 
for i in range(0, col):
    g.write(voca_list[i])
    g.write('\n')
g.close()
print('voca.txt 파일 생성완료.')
