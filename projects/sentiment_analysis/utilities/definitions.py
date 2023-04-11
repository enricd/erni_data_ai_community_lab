sentiment_info ="""#### What is sentiment analysis 
Sentiment analysis is the process of using Natural Language Processing to analyze digital text to determine if the emotional tone of the message is positive, negative, or neutral. 
Nowadays, companies have large volumes of text data like emails, customer support chat transcripts, social media comments, and reviews. 
Sentiment analysis tools can scan this text to automatically determine the author’s attitude towards a topic. 
Companies use the insights from sentiment analysis to improve customer service and increase brand reputation. """

project_description = """#### The challenge
In this project, we will use Tweepy, a library that can be used to access the Twitter API, and VADER (Valence Aware Dictionary for sEntiment Reasoning), 
which is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative/neutral) and intensity (strength) of emotion.
The purpose is to extract Tweets given a certain topic (Hashtag) and analyze the sentiment, as well as retrieving the most common words for each sentiment
to get deeper insights about public opinion.
"""

more_info = """#### More information
[Access to Twiter's API](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)\n
[VADER library](https://pypi.org/project/vaderSentiment/)\n
[VADER github homepage](https://github.com/cjhutto/vaderSentiment)\n
[Word Cloud library](https://pypi.org/project/wordcloud/) Note: This library only works with python 3.9 or below.\n
[Language detection library](https://pypi.org/project/langdetect/)
"""

how_to = """Fill the Hashtag field with the topic you want to analyze using # + the topic. E.g: "#ChatGPT".\n
Add the number of tweets you want to analyze in a range from 1 to 1000.\n
Note that the EDA page won't be filled until the model has run completely.\n
"""