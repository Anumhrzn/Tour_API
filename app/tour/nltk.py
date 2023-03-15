from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import string
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
lem = WordNetLemmatizer()

