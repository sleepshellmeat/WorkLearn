import numpy as np
from wordcloud import WordCloud
import PIL.Image as image
import jieba

arr = np.loadtxt('CSG.csv', dtype=str, usecols=(10), delimiter=",", skiprows=1)
text = ' '.join(arr)

word_list = jieba.cut(text)
result = ' '.join(word_list)

word = WordCloud(font_path='simsun.ttc').generate(result)
i = word.to_image()
i.show()

