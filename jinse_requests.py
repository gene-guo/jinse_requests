# 导入模块
import requests
import json


def parse(url):
    """
    用来发送请求获取数据  发送请求 获取响应
    :return: 文章列表
    """

    # 基础的反反爬措施 ————添加 user-agent   http协议中的一个字段  作用是：表示请求的客户端的身份
    # 为了使程序，模拟浏览器的身份，所以 我们需要给程序添加一个user-agent信息
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

    # 发送请求
    response = requests.get(url, headers=headers)  # 获取response对象


    # 获取响应
    result = response.content.decode()


    # 进行数据类型的转换  json str  ==>   dict
    dict_data = json.loads(result)

    # 获取文章列表
    article_list = dict_data['list']

    return article_list


def get_date(article_list):
    """
    处理数据，整合
    :param article_list:
    :return: 数据
    """
    # 盛放数据的列表
    data_list = []

    # 获取每一篇文章的信息
    for article in article_list:
        title = article['title']

        # 如果有content键，就应该能够返回数据，如果没有这个键，返回的是None
        if article['extra'].get('content'):
            summary = article['extra'].get('content')

        elif article['extra'].get('summary'):
            summary = article['extra'].get('summary')

        else:
            summary = ''

        # 获取详情页id
        child_id = article['extra']['child_id']

        # 组装数据
        data_list.append((title, summary, child_id))

    return data_list


def next_page(article_list):
    """
    获取下一页的url
    :param article_list:
    :return:
    """

    # 第二页 使用了第一页最后一篇文章的id构成了第二页的地址
    # 获取文章列表中的最后一片文章id
    last_article = article_list[-1]
    last_id = last_article['id']

    # 构造下一页的请求地址
    temp_url = 'https://api.jinse.com/v6/www/information/list?catelogue_key=www&limit=23&information_id={}&flag=down&version=9.9.9&_source=www'

    next_url = temp_url.format(last_id)

    return next_url


def main():

    url = 'https://api.jinse.com/v6/www/information/list?catelogue_key=www&limit=23&information_id=16970&flag=down&version=9.9.9&_source=www'

    i = 1

    while i < 2:
        # 发送请求，获取响应
        article_list  = parse(url)

        # 提取数据
        result = get_date(article_list)

        # 进行数据的保存

        next_url = next_page(article_list)

        url = next_url

        i += 1


if __name__ == '__main__':
    main()