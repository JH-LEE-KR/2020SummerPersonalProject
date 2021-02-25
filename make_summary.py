from readCsv import getTitles, getContents
import csv
import numpy as np
from konlpy.tag import Kkma
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

kkma = Kkma()

list_titles = getTitles()
list_contents = getContents()

f = open('summaries.csv', 'w', newline="\n", encoding='utf-8')
writer = csv.writer(f)

for contents in list_contents:
    list_sentences = []
    list_temp = kkma.sentences(contents)
    for i in range(len(list_temp)):
        if len(list_temp[i]) > 10: # 10자 미만은 너무 짧아 의미 없는 문장으로 가정하고 제거해준다.
            list_sentences.append(list_temp[i])
    tfidf = TfidfVectorizer()
    tfidf_sentence_matrix = tfidf.fit_transform(list_sentences).toarray()
    # 전치행렬과의 곱으로 그래프에서 어느 노드들이 엣지로 연결되었는지 나타내는 정사각 행렬 형태의 그래프를 생성한다.
    sentence_graph = linear_kernel(tfidf_sentence_matrix) # linear_kernel(A) -> A * transposed_A
    d = 0.85 # damping factor , PageRank에서 웹 서핑을 하는 사람이 해당 페이지를 만족하지 못하고 다른페이지로 이동하는 확률로써, TextRank에서도 그 값을 그대로 사용(0.85로 설정)
    A = sentence_graph 
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------
    for i in range(sentence_graph.shape[0]):
        A[i][i] = 0 # 자기 자신에 대한 값은 계산되면 안됨 -> 대각행렬 0으로 만들어준다.
        sum_row = np.sum(A[i][:])
        if sum_row != 0: # 그래프가 행렬의 대각 성분을 기준으로 대칭인 정사각 행렬이기 때문에 행, 열 어느 것을 택하든지 상관없다.
            A[i][:] /= sum_row # textrank formula에서 한 노드와 연결된 다른 노드들의 가중치값을 나누는 부분 -> 이후 상수에 반영.
        A[i][:] *= -d # TR(Vi) = (1-d) + d * sum(가중치*TR(Vj)) -> TR(Vi) - d(c1TR(Va) + c2TR(Vb) + c3TR(Vc) + c4TR(Vd)) = 1 - d (c1, c2, c3, c4 is constant) ->Ax=B
        A[i][i] = 1 # 자기 자신에 대한 값 다시 적용
    B = (1 - d) * np.ones((sentence_graph.shape[0], 1))
    textrank = np.linalg.solve(A, B) # x = [TR(Va), TR(Vb), TR(Vc), TR(Vd)] -> each textrank
    # 수식 계산에 대한 아이디어는 인터넷 자료를 인용함.
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------
    idx_textrank = []
    for i in range(len(textrank)):
        temp = [i, textrank[i]] 
        idx_textrank.append(temp) # [인덱스, textrank 점수]를 원소로 갖는 2차원 리스트 생성
    sorted_textrank = sorted(idx_textrank, key = lambda x: x[1], reverse = True) # textrank 점수를 기준으로 정렬
    contents = ""
    summaries = []
    for idx in sorted_textrank[:5]:
        contents  = contents + list_sentences[idx[0]]
    summaries.append(contents)
    for summary in summaries:
        writer.writerow([summary])

f.close()