from nis import match
from urllib.error import URLError
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


class Crwaler:
    def crwal(self, keyword):
        goods_list = []  # 크롤링하여 필터링된 데이터들
        for good in Crwaler.check_quasarzone(p=re.compile(f".*{keyword}")) : goods_list.append(good) # 키워드에 대한 정규표현식
        for good in Crwaler.check_coolenjoy(p=re.compile(f".*{keyword}")) : goods_list.append(good)
        for good in Crwaler.check_ppomppu(p=re.compile(f".*{keyword}")) : goods_list.append(good)
        return goods_list

    def check_quasarzone(p, url="https://quasarzone.com/bbs/qb_saleinfo"):
        html = urlopen(url)
        bs = BeautifulSoup(html, "html.parser")
        goods_list = []

        for info_goods in bs.findAll('span', {"class": "ellipsis-with-reply-cnt"}):
            if p.search(info_goods.get_text()):
                goods_text = info_goods.get_text()
                link = "https://quasarzone.com" + info_goods.parent['href']
                goods_list.append((goods_text, link))
        return goods_list

    def check_coolenjoy(p, url="https://coolenjoy.net/bbs/jirum"):
        html = urlopen(url)
        bs = BeautifulSoup(html, "html.parser")
        goods_list = []

        for info_goods in bs.findAll('td', {'class': 'td_subject'}):
            if p.search(info_goods.a.get_text()):
                goods_text = info_goods.a.get_text().lstrip()
                link = info_goods.a['href']
                goods_list.append((goods_text, link))
        return goods_list

    def check_ppomppu(p, url="https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu"):
        html = urlopen(url)
        bs = BeautifulSoup(html, "html.parser")
        goods_list = []

        for info_goods in bs.findAll('font', {'class': 'list_title'}):
            if p.search(info_goods.get_text()):
                goods_text = info_goods.get_text()
                link = "https://www.ppomppu.co.kr/zboard/" + \
                    info_goods.parent['href']
                goods_list.append((goods_text, link))
        return goods_list