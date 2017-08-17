from spider import url_manager, html_downloader, html_pasrer, html_outputer

class spiderMain(object):
    def __init__(self):
        self.urls = url_manager.Urlmanager()
        self.downLoader = html_downloader.downLoader()
        self.pasrer = html_pasrer.Pasrer()
        self.outPuter = html_outputer.outPuter()

    
    def carw(self, root_url):
        count = 1
        self.urls.addNewurl(root_url)
        while self.urls.hasNewurl():
            if count > 100:
                break
            new_url = self.urls.getNewurl()
            html_cont = self.downLoader.downLoad(new_url)
            new_urls,new_data = self.pasrer.pasre(new_url,html_cont)  
            self.urls.addNewurls(new_urls)
            self.outPuter.collget(new_data)
            count = count + 1
        self.outPuter.outHtml()
            
            
    
if __name__ =="__main__":
    root_url = "http://baike.baidu.com/link?url=G4g2Y2adGVw1V1mIjHVAr7xys9sVpEBpCEzNn1i7bSvPWuXSK35P84Beq-tVyZYQnQdYuC1Rm85s8TTuN9xW5q"
    obj_spider = spiderMain()
    obj_spider.carw(root_url)
    
