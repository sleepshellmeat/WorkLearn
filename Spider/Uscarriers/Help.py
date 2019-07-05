import numpy as np
from wordcloud import WordCloud
import PIL.Image as image
import jieba

def tran_CN(text):
    word_list = jieba.cut(text)
    result = " ".join(word_list)
    return result

# arr=np.loadtxt('CSG.csv',usecols=(1,2), delimiter=",",skiprows=1)
arr = np.loadtxt('CSG.csv', usecols=(12), dtype=str, delimiter=",", skiprows=1)
string = ','.join(arr)
text = tran_CN(string)
print(arr)
word = WordCloud().generate(text)
# word = WordCloud().fit_words(frequencies)  #根据词频生成词云
# word = WordCloud().generate_from_frequencies(frequencies[, ...])   #根据词频生成词云
# word = WordCloud().generate_from_text(text)    #根据文本生成词云
# word = WordCloud().process_text(string)  #将长文本分词并去除屏蔽词（此处指英语，中文分词还是需要自己用别的库先行实现，使用上面的 fit_words(frequencies) ）
# word = WordCloud().recolor([random_state, color_func, colormap])   #对现有输出重新着色。重新上色会比重新生成整个词云快很多
# word = WordCloud().to_array()  #转化为 numpy array
# word = WordCloud().to_file(filename)   #输出到文件

# i = word.to_image()
# i.show()

