
import requests
url = 'https://www.douban.com/'
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.douban.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

resp = requests.post(url,header)
resp.encoding = 'UTF-8'

print(resp.text)
print('--------------------------------')
print(resp.content)
print('--------------------------------')
print(resp.headers)
print('--------------------------------')
print(resp.url)