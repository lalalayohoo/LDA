import collections
import wordcloud                    # 词云展示库
#from PIL import Image               # 图像处理库
import matplotlib.pyplot as plt     # 图像展示库

def make_dict():
    f = open('..\data\model-00200.twords', 'r', encoding='utf-8')
    contect= f.read()
    f.close()
    lines=contect.split('\n')
    twords_num=40
    global words_list
    words_list = []
    for i in range(len(lines)):
        if i%(twords_num+1)==0:
            word_list=[]
            continue
    
        word_list.append(lines[i].split())
        if (i+1)%(twords_num+1)==0:
            word_list=dict(word_list)
            word_list=dict([(x,float(y)) for x,y in word_list.items()])
            words_list.append(word_list)



def make_wordcloud(i):
    wc = wordcloud.WordCloud(
        background_color='white',  # 设置背景颜色
        font_path='simfang.ttf',  # 设置字体格式

        max_words=50,  # 最多显示词数
        max_font_size=100,  # 字体最大值
        scale=5  # 调整图片清晰度，值越大越清楚
    )
    word_counts=collections.Counter(words_list[i])
    wc.generate_from_frequencies(word_counts) # 从字典生成词云
    wc.to_file("Topic "+str(i)+".png") # 将图片输出为文件
    #plt.imshow(wc) # 显示词云
    #plt.axis('off') # 关闭坐标轴
    #plt.show() # 显示图像



if __name__=='__main__':
    make_dict()
    for i in range(len(words_list)):
        make_wordcloud(i)

