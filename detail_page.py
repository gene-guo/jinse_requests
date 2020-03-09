#每一篇的url
#https://www.jinse.com/lives/152285.html
#https://www.jinse.com/blockchain/602625.html
#https://www.jinse.com/news/blockchain/602581.html

from save_data import data_to_db

tem_url = 'https://api.jinse.com/v6/topic/info?topic_id={}'

child_id = 601484

url = tem_url.format(child_id)
import requests
import json

headers = {
        'referer': 'https://www.jinse.com/blockchain/601484.html',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
#发送请求

response = requests.get(url, headers=headers)
res = response.content.decode()
res_dict = json.loads(res)
#获取提取数据
title = res_dict['title']


summary = res_dict['summary']

author = res_dict['author']

tags = res_dict['tags']

tags_str = '-'.join(tags)

content = res_dict['show_content']
import re

pattern = re.compile(r'<[^>]+>',re.S)
content = pattern.sub('', content)
#保存数据
sql = 'insert into news (title, summary, author, tag, content, child_id) values ("%s", "%s", "%s", "%s", "%s", %d)' % (title, summary, author, tags_str, content, child_id)

data_to_db(sql)