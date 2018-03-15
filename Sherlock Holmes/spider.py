# encoding = 'utf-8'
import requests
from requests import RequestException
from pyquery import PyQuery as pq


# 使用requests请求主网页，获取response内容
def get_main_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            res = response.text
            r = res.encode('ISO-8859-1').decode(response.apparent_encoding)
            return r
        return None
    except RequestException:
        return None


# 解析response，获取每章页码后缀，返回每章网址
def parse_main_page(html):
    doc = pq(html)
    attrs = doc('.dir .ccss a')
    parse_list = []
    for attr in attrs.items():
        parse_list.append(attr.attr.href)
    parse_list = parse_list[:-1]
    parse_lists = ['https://www.555zw.com/book/9/9938/' + attr for attr in parse_list]
    return parse_lists


# 使用pyquery请求每章网址并解析获取标题与内容
def parse_page(url):
    doc = pq(url, encoding='gbk')
    title = doc('.article_listtitle').text()
    article = doc('#content').text()
    data = title + '\n' + article
    return data


# 写入到txt文件
def write_to_txt(data):
    with open('Sherlock_Holmes.txt', 'a', encoding='utf-8') as f:
        f.write(data)


# 主函数。。。
def main():
    main_url = 'https://www.555zw.com/book/9/9938/index.html'
    html = get_main_page(main_url)
    urls = parse_main_page(html)
    for url in urls:               # 从parse_lists中取出每章网址
        data = parse_page(url)
        print(data)
        write_to_txt(data)


if __name__ == '__main__':
    main()
