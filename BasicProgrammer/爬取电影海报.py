# coding: utf-8
from selenium import webdriver
from lxml import etree
import os
import requests
import re

searchMovieKeys = '刘亦菲'
MAX_PAGE = 6

def download(src, imgId):
    img_dir = './'+searchMovieKeys+'/'
    # 对imgId做字符串处理，删除字符串中的？
    imgId = re.sub(r'[?]', '', str(imgId))
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    try:
        response = requests.get(src, timeout=10)
        if response.status_code == 200:
            file_path = img_dir + imgId + '.jpg'
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            print('Already downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to download')

def getMovieImages(page):
    print('正在下载第', page+1, '页')
    page = page * 15
    url = 'https://movie.douban.com/subject_search?search_text=' \
    + searchMovieKeys + '&cat=1002&start=' + str(page)
    driver = webdriver.Chrome('d:\\commonSoft\\chromedriver.exe')
    driver.get(url)
    # print(driver.page_source)
    # 3. 提取数据，lxml 进行 XPath 定位
    html = etree.HTML(driver.page_source)
    src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
    srcs = html.xpath(src_xpath)
    # print(srcs)
    titles = html.xpath(title_xpath)
    # 这里需要多个变量的for循环，用zip()
    for src, title in zip(srcs, titles):
        print('\t'.join([str(title.text), str(src)]))
        download(src, title.text)
    print('download finish')
    driver.close()
       

if __name__ == '__main__':
    for i in range(0, MAX_PAGE):
        getMovieImages(i)
