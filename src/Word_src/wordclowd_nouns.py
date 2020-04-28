import csv
import nltk
import numpy as np
from PIL import Image
from konlpy.tag import Okt
import matplotlib as npl
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib.font_manager as fn
font_name=fn.FontProperties(fname="C:/WIndows/Fonts/malgun.ttf").get_name()  #한글 꺠짐 패치
plt.rc("font",family=font_name)
burger_mask=np.array(Image.open("C:/Users/kjjs1/PycharmProjects/wordcount/data/burger_mask.jpg"))
npl.rcParams["axes.unicode_minus"]=False

num=1109

def main():
    text = str()
    stop_words = ["제", "월", "일", "조", "수", "때", "그", "이", "바", "및", "안", "정", "위", "관", "등", "외"
        , "여", "자", "통", "인", "회", "직", "겸", "중","철","로","역시","양준","나","내","거","은","는","이","가","ㅋ",",","!","?","ㅠ","ㅜ","ㄱ","ㄴ","ㄷ","~","is"] #필터링 하고 싶은 단어들을 넣으면 됩니다
    csv_open=open('C:/Users/kjjs1/PycharmProjects/WebCroll/comment(iron).csv','r', encoding='utf-8-sig') #저희 파일에 맞춰서 utf-8-sig 인코딩형식으로 열개 두었습니다.

    rdr=csv.reader(csv_open)
    text_list=list(rdr)
    output_file_name = "count.csv"

    csv_open.close()  # 파일 close
    open_output_file = open(output_file_name, 'w', -1, "euc-kr")

    for i in text_list:
        if i!=[]:
            text+=str(i[2])
    #print(text)
    t=Okt()
    comment_token=t.nouns(text)
    comment_word=[word for word in comment_token if word not in stop_words]

    count=nltk.Text(comment_word)
    list_count=count.vocab().most_common(num)
    all_count=count.vocab().most_common()
    #print(all_count)
    #open_output_file.write(str(all_count))
    for i in all_count:
        open_output_file.write(str(i)+'\n')
    wc=WordCloud(mask=burger_mask,font_path="C:/WIndows/Fonts/malgun.ttf").generate_from_frequencies(dict(list_count))
    plt.figure(figsize=(20,20))
    plt.imshow(wc,interpolation="bilinear")
    plt.axis("off")
   # plt.show()      # 이부분은 pycharm에서 돌릴때 추가된 부분입니다 jupyter notebook 에서는 필요없는걸로 알고 있습니다.
    open_output_file.close()
    plt.savefig("곽철용({}).png".format(num))
    print("done",len(all_count))
if __name__ == '__main__':
    main()