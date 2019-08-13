import numpy as np
from wordcloud import WordCloud
import PIL.Image as image
import jieba

# np.loadtxt是用来读取txt文件
# skiprows=1，是用来跳过第一行，一般来说第一行只是一个索引，应从第二行取数据
# dtype=str 用来设置读取数据的类型
# comments='#' 如果行的开头为'#'则会跳过该行，符号可以自己设置,不一定非要#
## usecols=(0, 2) 使用0-2两列，左闭右开，另外搭配的还有一个参数为unpack=True,使用后会使0-2行成为独立的两列，默认是合并一起的
# delimiter 为参数分割符
arr = np.loadtxt('CSG.csv', dtype=str, usecols=(10), delimiter=",", skiprows=1)
text = ' '.join(arr)

word_list = jieba.cut(text)
result = ' '.join(word_list)

word = WordCloud(font_path='simsun.ttc').generate(result)
i = word.to_image()
i.show()

