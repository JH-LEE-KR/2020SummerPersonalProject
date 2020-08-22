from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from split import splitArticles


list_title = splitArticles('title', '\n') # Get title that '\n' has been removed to compare similarity
list_contents = splitArticles('contents', '\n') # Get contents that '\n' has been removed to compare similarity


tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(list_contents) # Vectorize the frequency of each word in contents and Return normalized TF-IDF matrix


# Since it was normalized using fit_transform(), the cosine similarity can be obtained by dot product of TF-IDF matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix) # linear_kernel -> Calculate dot product of vectors

# function of providing a list of articles with a high similarity with a particular article
def get_similar(title, cosine_sim = cosine_sim):
    index = list_title.index(title) # Get the index of a particular article
    sim_scores = list(enumerate(cosine_sim[index])) # enumerate -> To create sequence pairs between article content and words
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse=True) # Similarities are expressed in sim_scores[1] -> key = lambda x: x[1], reverse=True -> descending order
    sim_scores = sim_scores[1:6] # In order to use only the top 5 articles with similarity.
    indices = [i[0] for i in sim_scores] # Index is expressed in sim_scores[0] -> i[0] for i in sim_scores
    sim_title = [] # To make a list of the titles of articles
    for i in indices:
        sim_title.append(list_title[i])
    return sim_title # Return list of titles for 5 articles with high similarity

