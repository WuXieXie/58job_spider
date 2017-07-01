class UrlManger(object):
    def __init__(self):
        self.new_urls=set() #收集的页面Url
        self.old_urls=set() #爬过的页面Url
        self.new_job_urls = set() #收集的Job的Url
        self.old_job_urls = set() #已经爬过的Job的Url

    def add_new_url(self, url): #添加页面Url 用以爬取Job url 单条加入
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls): #添加页面Urls
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self): #是否还有未爬取的页面Url
        return len(self.new_urls) != 0

    def get_new_url(self): #随机获取一条页面Url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_job_url(self, url):
        if url is None:
            return
        if url not in self.new_job_urls and url not in self.old_job_urls:
            self.new_job_urls.add(url)

    def add_new_job_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_job_url(url)

    def has_new_job_url(self):
        return len(self.new_job_urls) != 0

    def get_new_job_url(self):
        new_url = self.new_job_urls.pop()
        self.old_job_urls.add(new_url)
        return new_url