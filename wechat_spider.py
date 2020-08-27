import requests  # 请求网页
import os  # 用于创建文件夹
from lxml import etree  # 使用其中的xpath


def start():
    # 第一层，获取公众号全部文章的链接
    # filename =’.\source’  # 之前存在本地的公众号源代码
    with open(r'C:\Users\xionghao\PycharmProjects\test\source', 'r', encoding='utf-8')as f:
        source = f.read()  # 读取内容
    html_ele = etree.HTML(source)  # xpath常规操作
    hrefs = html_ele.xpath('//div[contains(@data-type,"IMG")]/h4/@hrefs')  # 锁定元素位置
    times=html_ele.xpath('string(//p[@class="weui_media_extra_info"]')
    num = 0
    for i in hrefs:
        num += 1
        try:
            apply_one(i)
            # print(i)
        except:
            continue
        # print('第%d篇爬取完毕' % num)


# 第二层，解析单篇文章
def apply_one(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.58'
    }

    response = requests.get(url, headers=headers)
    elements = etree.HTML(response.text)
    data_src = elements.xpath('//div[contains(@class,"share_media")]/img/@src')
    for src in data_src:
        try:
            print(src)
            download(src)  # 下载图片
        except:
            pass

# 第三层下载层
def download(src):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.58'}
    response = requests.get(src, headers=headers)
    name = src.split('/')[-2]# 截取文件名
    dtype = src.split('=')[-1]  # 截取图片类型
    name += '.' + dtype  # 重构图片名
    os.makedirs('dog', exist_ok=True)  # 当前目录生成doge文件夹

    with open('dog/' + name, 'wb')as f:
        f.write(response.content)
if __name__ == '__main__':
        start()