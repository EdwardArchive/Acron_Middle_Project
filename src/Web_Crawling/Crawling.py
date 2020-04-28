from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
fw = open('comment.txt','w', encoding='utf8')
csv_open=open('comment(nomal).csv','w', encoding='utf-8-sig')
f_csv=csv.writer(csv_open, dialect='excel')
driver = wd.Chrome(executable_path="chromedriver.exe")  #크롬 작동을 제어하는 모듈
url = 'https://www.youtube.com/watch?v=ESvz3xOa9R0' #  댓글을 받고 싶은 주소
urltest = 'https://www.youtube.com/watch?v=LNIpr3efeeI'
driver.get(url)
time.sleep(6.0)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height
html_source = driver.page_source
driver.close()

soup = BeautifulSoup(html_source, 'lxml')

youtube_user_IDs = soup.select('div#header-author > a > span')
youtube_comments = soup.select('yt-formatted-string#content-text')

str_youtube_userIDs = []
str_youtube_comments = []
for i in range(len(youtube_user_IDs)):
    str_tmp = str(youtube_user_IDs[i].text)
# print(str_tmp)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ','')
    str_youtube_userIDs.append(str_tmp)
    str_tmp = str(youtube_comments[i].text)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ', ' ')
    str_youtube_comments.append(str_tmp)
data={}
for i in range(len(str_youtube_userIDs)):
    #print(i+1,': ',str_youtube_userIDs[i],' : ', str_youtube_comments[i])
    textstr=str(i + 1)+ ': '+str_youtube_userIDs[i]+' : '+str_youtube_comments[i]+'\n'
    fw.writelines(textstr)
    csv_str=[str(i + 1),str_youtube_userIDs[i],str_youtube_comments[i]]
    data[str_youtube_userIDs[i]]=str_youtube_comments[i]
    f_csv.writerow(csv_str)
comments=pd.DataFrame(data,columns=["id","comments"])
print(comments)
fw.close()
csv_open.close()


