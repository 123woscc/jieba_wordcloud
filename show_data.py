# coding=utf-8
from os import path
from wordcloud import WordCloud
import codecs
from scipy.misc import imread

d = path.dirname(__file__)

# Read the whole text.
data = codecs.open("data.txt", "r", 'utf-8').read().split(' ')
num = range(1, len(data))[::-1]
final_data = zip(data, num)

text = codecs.open("data.txt", "r", 'utf-8').read()

# test_data=[('词a', 100),('词b', 90),('词c', 80)]
# Generate a word cloud image
# wordcloud = WordCloud(font_path='simhei.ttf').generate(text)

mask_img = imread('./heart-mask.jpg', flatten=True)

wordcloud = WordCloud(
    font_path='simhei.ttf',
    background_color='white',
    mask=mask_img
).generate_from_frequencies(final_data)

import matplotlib.pyplot as plt

plt.imshow(wordcloud)
plt.axis("off")

plt.show()
