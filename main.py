import re

from selenium import webdriver
from selenium.webdriver import ChromeOptions

from CacaMusicSpider import *


class NetEaseMusicSpider(MusicSpider):
    def __init__(self):
        super().__init__()
        self.url = 'https://music.163.com'
        self.page_url = 'https://music.163.com/#/song'
        self.outer_url = 'https://music.163.com/song/media/outer/url'
        self.file_suffix = '.mp3'

    def download_get_info(self, id):
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        page = f'{self.page_url}?id={id}'
        driver.get(page)
        title = driver.title
        regex_tit = re.match('^(.*?) - (.*?) - .*? - .*?$', title)
        song = SongInfo(
            id=id,
            outer_url=urljoin(self.outer_url, '?id=' + str(id)),
            title=regex_tit.group(1),
            singer=regex_tit.group(2),
            platform='NetEase',
            url=page
        )
        return song


def self_run():
    print("欢迎来到CACA歌曲下载系统:网易云引擎单机版")
    spider = NetEaseMusicSpider()
    while True:
        id = input("请输入要下载的id:")
        download = spider.download(id)
        print(f'{download} 下载成功！')
        if input('Again?(y/N):') != 'y':
            break


if __name__ == '__main__':
    self_run()
