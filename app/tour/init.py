# Content Based Filtering
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

lem = WordNetLemmatizer()

csv = pd.read_csv("app/tour/review_with_rating.csv", encoding='utf-8')
dataframe_places = pd.DataFrame(csv.groupby("Place")["Review Body"].apply(list)).reset_index()
dataframe_places["Review Body"] = dataframe_places["Review Body"].apply(lambda x: ' '.join(x))

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(dataframe_places['Review Body'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Collaborative Based Filtering
ratings = pd.read_csv("app/tour/Collaborative Final.csv", encoding='utf-8')

agg_ratings = ratings.groupby('places').agg(mean_rating=('ratings', 'mean'),
                                            number_of_ratings=('ratings', 'count')).reset_index()
agg_ratings_GT100 = agg_ratings[agg_ratings['number_of_ratings'] > 2]
df_GT100 = pd.merge(
    ratings, agg_ratings_GT100[['places']], on='places', how='inner')
matrix = df_GT100.pivot_table(
    index='userid', columns='places', values='ratings')
matrix_norm = matrix.subtract(matrix.mean(axis=1), axis='rows')
user_similarity = matrix_norm.T.corr()
