
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_urls(self, soup):
        new_urls = set()
        # 可使用正则
        links = soup.find_all('div',class_='item clearfix')
        print()
        for link in links:
            new_url=link['data-href']
            # 拼接Url
            # new_full_url=urlparse(page_url,new_url)
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self,page_url, soup):
        res_data = {}
        # url
        url = page_url
        res_data['Url'] = url
        # title
        title_node = soup.find('div',class_='zw clearfix').find('h1')
        res_data['Title'] = title_node.get_text()
        res_data['Title'].encode('gbk')
        # money
        price_node = soup.find('div',class_='price').find('span')
        res_data['Price'] = price_node.get_text()
        res_data['Price'].encode('gbk')
        # Company
        company_node = soup.find('div',class_='gsjs1').find('h2').find('a')
        res_data['Company'] = company_node.get_text()
        res_data['Company'].encode('gbk')
        # describe
        describe_node = soup.find('p')
        res_data['Describle'] = describe_node.get_text()
        res_data['Describle'].encode('gbk')
        # 调试输出数据
        print (res_data)
        return res_data
    def parse(self,html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser')
        new_urls = self._get_new_urls(soup)
        return new_urls

    def parse_job(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser')
        new_data = self._get_new_data(page_url,soup)
        return new_data

    def get_page_num(self,html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser')
        page_num_all = soup.find('input',id='totalPage')
        page_num = page_num_all['value']
        return page_num



