import urllib
import urllib.request
import urllib.parse
from collections import deque
import difflib
import string
from typing import (
    List, Tuple
)
import re


class OpenFiles(object):
    def __init__(self, files: List[str] or Tuple[str] = None, mode: str = 'r', encoding: str = 'utf-8') -> None:
        if files is None:
            self.__files = []
        else:
            self.__files = list(files)
        self.__mode = mode
        self.__encoding = encoding
        self.__fds = []

    def __enter__(self) -> List:
        for f in self.__files:
            self.__fds.append(open(f, self.__mode, encoding=self.__encoding))
        return self.fds

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        for fd in self.fds:
            fd.close()

    @property
    def fds(self) -> List:
        return self.__fds


def read_file(file_path: List[str] or Tuple[str]) -> List:
    files = []
    with OpenFiles(file_path) as fds:
        for fd in fds:
            files.append(fd.read())
    return files


import http.cookiejar


# head: dict of header
def make_my_opener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def main():
    que = deque()
    visited = set()

    url = 'https://www.baidu.com/'
    que.append(url)
    cnt = 0

    while que:
        url = que.popleft()
        visited |= {url}

        print('已经抓取: ' + str(cnt) + '个    正在抓取 <--- ' + url)
        cnt += 1

        try:
            urlop = urllib.request.urlopen(url, timeout=2)
            if 'html' not in urlop.getheader('Content-Type'):
                continue
            data = urlop.read().decode('utf-8')
        except:
            continue

        linkre = re.compile(r'href="(.+?)"')
        for x in linkre.findall(data):
            if 'http' == x[:4] and x not in visited:
                # x = urllib.parse.quote(x, safe=string.printable)
                que.append(x)
                print('加入队列 --->  ' + x)


if __name__ == '__main__':
    oper = make_my_opener()
    uop = oper.open('http://www.baidu.com/', timeout=1000)
    data = uop.read()
    print(data.decode())

# subprocess.run(['dir', '.'], shell = True, stdout =  subprocess.PIPE)
