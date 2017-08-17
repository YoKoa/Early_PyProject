
from bs4 import BeautifulSoup
import re

class Pasrer(object):
    
    
    def new_url_pares(self, page_url,soup):
        links = soup.find_all('a',href = re.compile("/view"))
        return links
    
    
    def neew_data_pares(self, page_url,soup):
        data = {}
        
        data['url'] = page_url
        
        title_node = soup.find('dd',class_="title").find('h1',class_="python")
        data['title'] = title_node.get_text()
        
        summary_node = soup.find('div')
        data['summary'] = summary_node.get_text()
        
        
    
    def pasre(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_url = self.new_url_pares(page_url,soup)
        new_date = self.neew_data_pares(page_url,soup)
        return new_url,new_date
    
    
    



