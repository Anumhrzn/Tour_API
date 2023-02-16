# Data processing
import pandas as pd
import numpy as np

ratings=pd.read_csv('Collaborative Final.csv')
ratings.head()

agg_ratings = ratings.groupby('places').agg(mean_rating = ('ratings', 'mean'),
                                                number_of_ratings = ('ratings', 'count')).reset_index()

agg_ratings_GT100 = agg_ratings[agg_ratings['number_of_ratings']>2]

df_GT100 = pd.merge(ratings, agg_ratings_GT100[['places']], on='places', how='inner')

matrix = df_GT100.pivot_table(index='userid', columns='places', values='ratings')

matrix_norm = matrix.subtract(matrix.mean(axis=1), axis = 'rows')

user_similarity = matrix_norm.T.corr()

picked_userid = 13
user_similarity.drop(index=picked_userid, inplace=True)

n = 10
user_similarity_threshold = 0.3
similar_users = user_similarity[user_similarity[picked_userid]>user_similarity_threshold][picked_userid].sort_values(ascending=False)[:n]
print(f'The similar users for user {picked_userid} are', similar_users)

picked_userid_visited = matrix_norm[matrix_norm.index == picked_userid].dropna(axis=1, how='all')

similar_user_places = matrix_norm[matrix_norm.index.isin(similar_users.index)].dropna(axis=1, how='all')

similar_user_places.drop(picked_userid_visited.columns,axis=1, inplace=True, errors='ignore')

item_score = {}
for i in similar_user_places.columns:
  place_rating = similar_user_places[i]
  total = 0
  count = 0

  for u in similar_users.index:
    if pd.isna(place_rating[u]) == False:
      score = similar_users[u] * place_rating[u]
      total += score
      count +=1
  item_score[i] = total / count
item_score = pd.DataFrame(item_score.items(), columns=['Place', 'Place_score'])
    
ranked_item_score = item_score.sort_values(by='Place_score', ascending=False)
m = 10
ranked_item_score.head(m)