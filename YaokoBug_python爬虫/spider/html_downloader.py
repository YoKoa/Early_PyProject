
import urllib
class downLoader(object):
    def downLoad(self,url):
        if url is None:
            return None
        resPonse = urllib.request.urlopen(url)
        
        if resPonse.getcode() != 200 :
            return None
        return resPonse.read()
    
    



