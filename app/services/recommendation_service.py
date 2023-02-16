from app.tour.init import lem,dataframe_places,csv,user_similarity,matrix_norm
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import string
import pandas as pd
stop_words = set(stopwords.words('english')) 
exclude = set(string.punctuation)
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from app.tour.init import cosine_sim

def filter_keywords(doc):
    doc=doc.lower()
    stop_free = " ".join([i for i in doc.split() if i not in stop_words])
    punc_free = "".join(ch for ch in stop_free if ch not in exclude)
    word_tokens = word_tokenize(punc_free)
    filtered_sentence = [(lem.lemmatize(w, "v")) for w in word_tokens]
    return filtered_sentence

def get_recommendations(title):
    dataframe_places['Review Body'] = dataframe_places['Review Body'].apply(filter_keywords)
    dataframe_places["Review Body"]=dataframe_places["Review Body"].apply(lambda x: ' '.join(x))
    # a = a.reset_index()
    titles = dataframe_places['Place']
    indices = pd.Series(dataframe_places.index, index=dataframe_places['Place'])
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    product_indices = [i[0] for i in sim_scores]
    print(titles.iloc[product_indices].tolist())
    return titles.iloc[product_indices].tolist()

def get_userid(picked_userid):
    user_similarity.drop(index=picked_userid, inplace=True)
    n = 10
    user_similarity_threshold = 0.3
    similar_users = user_similarity[user_similarity[picked_userid] >
                                    user_similarity_threshold][picked_userid].sort_values(ascending=False)[:n]
    print(f'The similar users for user {picked_userid} are', similar_users)

    picked_userid_visited = matrix_norm[matrix_norm.index == picked_userid].dropna(
        axis=1, how='all')

    similar_user_places = matrix_norm[matrix_norm.index.isin(
        similar_users.index)].dropna(axis=1, how='all')

    similar_user_places.drop(
        picked_userid_visited.columns, axis=1, inplace=True, errors='ignore')

    item_score = {}
    for i in similar_user_places.columns:
        place_rating = similar_user_places[i]
        total = 0
        count = 0

        for u in similar_users.index:
            if pd.isna(place_rating[u]) == False:
                score = similar_users[u] * place_rating[u]
                total += score
                count += 1
        item_score[i] = total / count

    item_score = pd.DataFrame(item_score.items(), columns=[
                              'Place', 'Place_score'])
    ranked_item_score = item_score.sort_values(
        by='Place_score', ascending=False)
    m = 10
    print(ranked_item_score['Place'].to_list())
    return ranked_item_score['Place'].to_list()