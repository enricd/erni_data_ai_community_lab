import tweepy
import pandas as pd
from langdetect import detect
from wordcloud import WordCloud, STOPWORDS

from projects.sentiment_analysis.utilities.settings import *


def tweet_importer(hashtag, number_of_tweets):
    # Authentication
    auth = tweepy.OAuthHandler(TWITTER_NLP_CONSUMER_KEY, TWITTER_NLP_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_NLP_ACCESS_KEY, TWITTER_NLP_ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Query
    found_tweets = [status._json['text'] for status in tweepy.Cursor(api.search_tweets, lang='en', q=hashtag).items(number_of_tweets)]
    
    # DataFrame
    df = pd.DataFrame(found_tweets)
    df.rename({0:'text'},axis='columns',inplace=True)
    df.drop_duplicates(inplace = True)
    return df

def tweet_cleaner(raw_text):
    text=re.sub('@[^\s]+',"", raw_text)        # Remove mentions
    text=re.sub('#[^\s]+',"",text)             # Remove hashtags
    text=re.sub(r"http\S+","", text)           # Remove media links
    text=re.sub('RT ', '', text)               # remove the RT
    text = re.sub(r'[^a-zA-Z0-9\s]+', '', text)
    text=emoji_pattern.sub(r'',text)
    text = text.lower()
    text = text.replace('\n', ' ')
    return  pd.Series([text])


def detect_language(text):
    try:
        src_lang = detect(text)
        return src_lang          
    except:
        return "NA"
    
def create_wordcloud(text, name):
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color='white', max_words=3000, stopwords=stopwords, repeat=True)
    wc.generate(str(text))
    output_path = f'projects/sentiment_analysis/images/wc_outputs/{name}.png'
    wc.to_file(output_path)
    return output_path

def count_values_in_column(data,feature):
    total=data.loc[:,feature].value_counts(dropna=False)
    percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])