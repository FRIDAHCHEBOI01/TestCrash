# Import the TextBlob library
from textblob import TextBlob

# Define a sentence or text to analyze

text='I like food.'

# Create a TextBlob object from the text
blob = TextBlob(text)

# Use the TextBlob object to get the sentiment polarity
polarity = blob.sentiment.polarity

# Check the sentiment polarity and print the result
if polarity > 0:
    print("Sentiment: Positive")
elif polarity == 0:
    print("Sentiment: Neutral")
else:
    print("Sentiment: Negative")
