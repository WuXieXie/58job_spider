# coding:utf8
from urllib.parse import urlparse

from Job58_spider import url_manger, html_downloader, html_parser, html_outputer
import requests
from bs4 import BeautifulSoup

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manger.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutput()

    def craw(self, root_url):
        #获取总页数
        html_cont = self.downloader.download(root_url)
        page_num = self.parser.get_page_num(html_cont)
        #添加所有页数进入页面Url管理器
        for page_now in range(1,int(page_num)+1):
            new_url = 'http://hz.58.com/xueshengjianzhi/1/pn' + str(page_now)
            self.urls.add_new_url(new_url)
        #爬取所有页面Url的Job Url
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('Craw %d : %s' % (count, new_url))
                count = count + 1
                html_cont = self.downloader.download(new_url)
                new_urls = self.parser.parse(html_cont)
                self.urls.add_new_job_urls(new_urls)
                print ('Have Craw %d urls' % len(new_urls))
            except:
                print('Craw Failed')

        count = 1
        while self.urls.has_new_job_url():
            try:
                new_job_url = self.urls.get_new_job_url()
                print('Craw %d : %s' % (count,new_job_url))
                count = count + 1
                html_job_cont = self.downloader.download(new_job_url)
                new_data = self.parser.parse_job(new_job_url,html_job_cont)
                self.outputer.collect_data(new_data)
            except:
                print('Craw Failed')

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = 'http://hz.58.com/xueshengjianzhi/1/pn1/'  # 入口Url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)