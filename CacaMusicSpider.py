from urllib.parse import urljoin

import requests


class MusicSpider:
    def __init__(self):
        self.url = ''
        self.page_url = ''
        self.outer_url = ''
        self.file_suffix = ''

    def download(self, id):
        info = self.download_get_info(id)
        name = f'{info.platform}[{info.id}]{info.title}:{info.singer}'
        outer_url = info.outer_url
        self.download_downloader(outer_url, name)
        return name

    def download_get_info(self, id):
        song = SongInfo(
            id=None,
            outer_url=None,
            title=None,
            singer=None,
            platform='Caca',
            url=None
        )
        return song

    def download_downloader(self, outer_url, name):
        file_name = name + self.file_suffix
        r = requests.get(outer_url)
        with open(file_name, 'wb') as f:
            f.write(r.content)
            f.close()


class SongInfo:
    def __init__(self, id, title, url, platform, singer=None, outer_url=None):
        self.outer_url = outer_url
        self.url = url
        self.singer = singer
        self.platform = platform
        self.id = id
        self.title = title
