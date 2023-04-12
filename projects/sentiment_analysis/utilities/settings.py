import os
import re

# Authentication keys
TWITTER_NLP_CONSUMER_KEY = 'gjysqfr4Jy8lAzIuxa8Hpu2VY'
TWITTER_NLP_CONSUMER_SECRET = 'C8ANS2lInCj8I1SinulfzQnbO0QWCdxglYpw8305UzUH7MUWGl'
TWITTER_NLP_ACCESS_KEY = '2788714541-Yy6bpudQA07wVAWIeUxd4SIRPfWP6ER4wAEINhN'
TWITTER_NLP_ACCESS_SECRET = 'VJPnRK1fVU9ztFimI9tOrD746oTpHeeXlqgtbjL0SFZt4'

#Emoji Patterns
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                           "]+", flags=re.UNICODE)