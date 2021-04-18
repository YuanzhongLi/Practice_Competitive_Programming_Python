import threading

def get_host_name(string):
    return string.split('/')[2:3]

class URLFetcher(threading.Thread):
    def __init__(self, url, host_name, htmlParser):
        threading.Thread.__init__(self)
        self.url = url
        self.host_name = host_name
        self.htmlParser = htmlParser
        self.new_urls = set()

    def run(self):
        self.get_urls()

    def get_urls(self):
        self.new_urls = set([u for u in self.htmlParser.getUrls(self.url) if self.host_name == get_host_name(u)])

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host_name = get_host_name(startUrl)
        q = [startUrl]
        visited = set(q)
        while q:
            next_level = set()
            threads = [URLFetcher(url, host_name, htmlParser) for url in q]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
                next_level |= thread.new_urls
            next_level -= visited
            visited |= next_level
            q = next_level
        return visited
