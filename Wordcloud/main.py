import pandas as pd
import numpy as np
import wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image


df=pd.read_csv("/Users/reham/Desktop/Wordcloud 2/CSV Cleaned data")
text = " ".join(review for review in df.SYMPTOM2.astype(str))
removethese= ["Injection", "site","test","COV","nan","NAN"] +list(STOPWORDS)
count = df['SYMPTOM2'].value_counts()
df['SYMPTOM2'].value_counts()[:5].plot(kind='barh')


cloudimage=WordCloud(stopwords=removethese,max_words=10000,width=2000, height=1000,background_color="white").generate(text)

plt.figure( figsize=[20,15])

plt.tight_layout(pad=0)

plt.imshow(cloudimage,interpolation='bilinear')
plt.axis("off")
plt.show()




# frequency count of column A
