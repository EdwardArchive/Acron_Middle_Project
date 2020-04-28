import csv
import numpy as np
import nltk
import matplotlib as npl
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import matplotlib.font_manager as fn
font_name=fn.FontProperties(fname="C:/WIndows/Fonts/malgun.ttf").get_name()  #한글 꺠짐 패치
plt.rc("font",family=font_name)


burger_mask=np.array(Image.open("C:/Users/kjjs1/PycharmProjects/wordcount/data/burger_mask.jpg"))

csv_text=csv.reader(open("C:/Users/kjjs1/PycharmProjects/wordcount/data/count수정_곽철용.csv",'r',encoding='euc-kr')) #파일 주소
word_count_dict={}
count=0
num=50
tmp_list=list(csv_text)
for i,j,_ in tmp_list:
    if(count<num):
        word_count_dict[i]=int(j)
print(len(word_count_dict))

wc=WordCloud(mask=burger_mask,font_path="C:/WIndows/Fonts/malgun.ttf").generate_from_frequencies(word_count_dict)
plt.figure(figsize=(20,20))
plt.imshow(wc,interpolation="bilinear")
plt.savefig("곽철용-형용사동사({}).png".format(num))
plt.axis("off")
plt.show()

