import csv
from konlpy.tag import Twitter
from collections import Counter
import pandas as pd
def get_tags(text, ntags=50):
    spliter = Twitter()
    # konlpy의 Twitter객체
    nouns = spliter.nouns(text)
    # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns)
    # Counter객체를 생성하고 참조변수 nouns할당
    return_list = []  # 명사 빈도수 저장할 변수
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장합니다.
    return return_list

csv_open=open('C:/Users/kjjs1/PycharmProjects/WebCroll/comment(nomal).csv','r', encoding='utf-8-sig') #저희 파일에 맞춰서 utf-8-sig 인코딩형식으로 열개 두었습니다.
rdr=csv.reader(csv_open)
data_str=list()
dic={"1번분류":("실화","너무","진짜","썸네일","썹네","궁금","기대","대박","봤","실홥","영상","이게","여기다","와우","윤계상","곽철용"
             ,"철용","계상","이정재","쟝첸","장첸","클라스","햄버거","버거킹"),
     "2번분류":("퀄리티", "보소","맛있겠다","강렬","군침","되겠","ㅋ","ㄷ","많겠","배고프","보면","보이","비싸","사이즈","새로워","ㅇㅈ","아주훌륭","아찔해","어캐먹어","얼굴"
             ,"오졌","입","있다","있습","좋겠다","크다","크당"),
     "3번분류":("가야","가야해","갈거","가즈아","고고씽","나가야","먹어","사먹겠다","사먹고싶지만","사먹어야지","시켜야"),
     "4번분류":("먹었","먹엇","먹어보","먹어봣","먹어봤","맛있는데","맛있다","맛있을","꿀맛","맛없","맛업","마싯","마시","노맛","마싯","맛시"
             ,"맛있","맜있","개꿀맛","개맛","존맛","꿀맛","괜찮던","괜춚","꿀이던데","나름",
                "남김","노맛","만족하고","맞있음","먹고싶","먹어봄","배부르","배불러서","버릴거야","사먹었는데","시켰는데","크던데","핵맛","핵존맛","후회되네")}   #검색하고 싶은 단어 문장 id:는 분류로
data={"words_comment_1":[],"words_count_1":0,"words_comment_2":[],"words_count_2":0,"words_comment_3":[],"words_count_3":0,"words_comment_4":[],"words_count_4":0} #comment는 해당 댓글을 저장 , count는 횟수
for line in rdr:
    if line != []:                      #기존에 파일에 있는 자료를 옮겨오는 과정입니다.
        data_str.append(tuple(line))
for i in data_str:
    check=False
    for item in range(4,0,-1):
        for tu in dic[str(item)+"번분류"]:
            if  tu in i[2] and check==False:                 #i[2]번위치는 리스트에서 댓글(문자열)의 위치입니다
                data["words_count_"+str(item)]=data["words_count_"+str(item)]+1 #언급된 횟수를 저장하는 곳입니다.
                data["words_comment_"+str(item)].append(i)  #해당댓글을 저장하는곳입니다.
                check=True

for item in range(1,5):
    data["words_comment_"+str(item)]=list(set(data["words_comment_"+str(item)]))
    print(item,"번 분류 에 대한 단어 횟수 ",len(data["words_comment_"+str(item)]))
    print("------------------------------------------------------------------------------------------------------------------------------------")
    for i in data["words_comment_"+str(item)]:
        print(i)
    print("\n==================================================================================================================================\n")
#datafram= pd.DataFrame(data)
print(len(dic["1번분류"]),len(dic["2번분류"]),len(dic["3번분류"]),len(dic["4번분류"]))
csv_open.close()