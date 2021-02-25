
with open('matrixInfo.txt','r') as t:
  row = int(t.readline()) #
  col = int(t.readline())

g=open("voca.txt", 'r', encoding='utf-8')
list_voca = g.read()
list_voca = list_voca.split('\n')

f = open("matrix.txt", 'r', encoding='utf-8')
list_matrix = []
matrix = f.read()
for i in range(0,row):
  temp1 = list(matrix.split('\n')) # 행 단위로 분리
  temp2 = list(temp1[i].split(',')) # 열 단위로 분리
  list_matrix.append(temp2)
f.close()



def get_FrequencyTitle(word):
  if(word.strip() == '') :
      return []

  try:
    index = list_voca.index(word) # 행렬 중 특정 단어의 인덱스를 리턴해줌
  except:
    print(word + "is not in vocabulary")
    return []

  frequency = [] 

  for i in range(0, row): # [index, frequency]를 원소로 갖는 2차원 리스트 생성
    temp = [i, (int(list_matrix[i][index]))] # temp = [index, frequency]
    frequency.append(temp)

  frequency = sorted(frequency, key = lambda x: x[1], reverse=True)
  frequency = frequency[0:5]
  return frequency 


def get_FrequencyWord(index):
    frequency = [] 
    for i in range(0, col): # [index, frequency]를 원소로 갖는 2차원 리스트 생성
        temp = [i, (int(list_matrix[index][i]))] # temp = [index, frequency]
        frequency.append(temp)
    frequency = sorted(frequency, key = lambda x: x[1], reverse=True) 
    frequency = frequency[0:5]
    indices = [i[0] for i in frequency] 
    rank_word = [] 
    for i in indices:
        rank_word.append(list_voca[i])
    return rank_word
