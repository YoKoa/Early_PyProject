


class Urlmanager(object):
    
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    
    
    
    def addNewurl(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def addNewurls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addNewurl(url)
    
    def hasNewurl(self):
        return len(self.new_urls) != 0

    def getNewurl(self):
        new_Url = self.new_urls.pop()
        self.old_urls.add(new_Url)
        return new_Url
    
    
    
    
    
    
    
    
        
    
    



