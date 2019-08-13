import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

def cut_word():
    with open('jd_comment.txt', 'r', encoding='utf-8') as fp:
        text_comment = fp.read()
        word_list = jieba.cut(text_comment, cut_all=True)
        wl = ''.join(word_list)
        return wl

def main():
    mk = np.array(Image.open('wawa.jpg'))
    wl = cut_word()
    word = WordCloud(font_path='simsun.ttc',background_color='white', max_words=2000, scale=4,
                     max_font_size=50, random_state=42, mask=mk)
    word.generate(wl)
    plt.imshow(word, interpolation='bilinear')
    plt.axis('off')
    plt.figure()
    plt.show()


if __name__ == '__main__':
    main()