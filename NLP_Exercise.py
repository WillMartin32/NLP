from nltk import text
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
from pathlib import Path
from operator import itemgetter
from wordcloud import WordCloud
import imageio

#nltk.download('stopwords')


stops = stopwords.words('english')

more_stops = ['thy', 'ye', 'verily', 'thee', 'hath', 'say', 'thou', 'art', 'shall']

stops += more_stops

blob = TextBlob(Path("book of John text (1).txt").read_text())

go = []

go += blob.noun_phrases

items = blob.word_counts.items()

clean_items = [i for i in items if i[0] in go and i[0] not in stops]

sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

limited_list = sorted_list[:15]


top_15 = ''

for i in limited_list:
    top_15 += i[0]
    top_15 += ' '


wordcloud = WordCloud(colormap='prism',background_color='white')

wordcloud = wordcloud.generate(top_15)

wordcloud = wordcloud.to_file("BookofJohn.png")

print('done')
