import requests
from bs4 import BeautifulSoup

# 目标url
url = 'http://www.biquw.com/book/1/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}


# 向目标url发送get请求
response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response, 'lxml')
#章节数据
data_list = soup.find('ul')
#二次筛选,获取所有a标签
for i in data_list.find_all('a'):
    book_url = 'http://www.biquw.com/book/1/' + i['href']
    # print(book_url)

    #再次请求获取小说内容页
    book_content = requests.get(book_url).text
    # print(book_content)
    soup = BeautifulSoup(book_content,'lxml')
    content = soup.find('div',{'id':'htmlContent'}).text
    # print(content)
    # break
    #写入文件
    with open('story.txt','w',encoding='utf-8') as f:
        f.write(content)
