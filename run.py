import urllib
import urllib.request
import urllib.parse
from collections import deque
import difflib
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


def main():
    que = deque()
    visited = set()

    url = 'https://www.douban.com/'
    que.append(url)
    cnt = 0

    while que:
        url = que.popleft()
        visited |= {url}

        print('已经抓取: ' + str(cnt) + '个    正在抓取 <--- ' + url)
        cnt += 1
        urlop = urllib.request.urlopen(url)
        if 'html' not in urlop.getheader('Content-Type'):
            continue

        try:
            data = urlop.read().decode('utf-8')
        except:
            continue

        linkre = re.compile('href="(.+?)"')
        for x in linkre.findall(data):
            if 'http' in x and x not in visited:
                que.append(x)
                print('加入队列 --->  ' + x)


if __name__ == '__main__':
    main()

# subprocess.run(['dir', '.'], shell = True, stdout =  subprocess.PIPE)
