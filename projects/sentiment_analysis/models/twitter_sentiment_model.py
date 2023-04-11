import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from projects.sentiment_analysis.utilities.helpers import *

class TwitterSentimentAnalyzer():
    def __init__(self, number_of_tweets, hashtag):
        self.number_of_tweets = number_of_tweets
        self.hashtag = hashtag
        self.data = pd.DataFrame()
        self.data_positive = pd.DataFrame()
        self.data_neutral  = pd.DataFrame()
        self.data_negative = pd.DataFrame()
        self.most_common_words = ""
        self.n_gram = []
        self.status = ""
        self.run_model()

    def data_ingestion(self):
        self.data = tweet_importer(self.hashtag, self.number_of_tweets)
        

    def data_cleaning(self):
        self.data['plain_text'] = self.data.text.apply(tweet_cleaner)
        self.data = self.data.replace(r'^\s*$', np.nan, regex=True)
        if self.data.isnull().sum().plain_text != 0:
            self.data.dropna(inplace=True)
        
        self.data['text_lang']=self.data.plain_text.apply(detect_language)
        self.data = self.data[self.data.text_lang == 'en']
        
    
    def sentiment_analysis(self):
        for index, row in self.data['plain_text'].items():
            score = SentimentIntensityAnalyzer().polarity_scores(row)
            neg = score['neg']
            neu = score['neu']
            pos = score['pos']
            comp = score['compound']
            if neg > pos:
                self.data.loc[index, 'sentiment'] = "Negative"
            elif pos > neg:
                self.data.loc[index, 'sentiment'] = "Positive"
            else:
                self.data.loc[index, 'sentiment'] = "Neutral"
            self.data.loc[index, 'neg'] = neg
            self.data.loc[index, 'neu'] = neu
            self.data.loc[index, 'pos'] = pos
            self.data.loc[index, 'compound'] = comp

        self.data_negative = self.data[self.data['sentiment']=='Negative']
        self.data_positive = self.data[self.data['sentiment']=='Positive']
        self.data_neutral  = self.data[self.data['sentiment']=='Neutral']
        

    def get_most_common_words(self):
        countVectorizer = CountVectorizer(stop_words='english') 
        countVector = countVectorizer.fit_transform(self.data['plain_text'])
        negative_count_vect_df = pd.DataFrame(countVector.toarray(), columns=countVectorizer.get_feature_names_out())

        count = pd.DataFrame(negative_count_vect_df.sum())
        self.most_common_words = count.sort_values(0,ascending=False).head(20)
        
    
    def get_top_n_gram(self,n=20):
        vec = CountVectorizer(ngram_range=(3,3),stop_words = 'english').fit(self.data['plain_text'])
        bag_of_words = vec.transform(self.data['plain_text'])
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
        self.n_gram = words_freq[:n]
        

    def run_model(self):
        self.data_ingestion()
        self.data_cleaning()
        self.sentiment_analysis()
        self.get_most_common_words()
        self.get_top_n_gram()
        self.status += "\nCompleted\n"