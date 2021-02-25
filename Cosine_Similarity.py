from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def get_similar(title, list_title,list_contents):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(list_contents).toarray()
    transpose_tfidf_matrix = np.transpose(tfidf_matrix)
    cosine_sim = np.dot(tfidf_matrix, transpose_tfidf_matrix) # TF-IDF 행렬과 그것의 전치행렬의 내적(dot product) -> 각 성분 = COSINE 유사도 점수
    index = list_title.index(title) 
    scores = []
    for i in range(len(cosine_sim[index])): 
        temp = [i, cosine_sim[index][i]] # [index]-> 행, 각 기사 [i] -> 열, 각 기사간 유사도 점수. 전치행렬과의 내적을 통해 얻어진 정사각행렬이기 때문에 행, 열 어느것을 사용하든 상관은 없다.
        scores.append(temp)
    scores = sorted(scores, key = lambda x: x[1], reverse=True) # 인덱스 순이 아닌 유사도 점수 순서로 정렬
    indices = []
    for i in range(len(scores)):
        indices.append(scores[i][0]) 
    indices = indices[1:6] # index 0은 자기 자신에 대한 값 즉, 유사도의 의미가 없음 -> index 1부터 시작한다.
    sim_title = []
    for i in indices:
        sim_title.append(list_title[i])
    return sim_title