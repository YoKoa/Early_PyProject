



class outPuter(object):
    def __init__(self):
        self.list = []
    
    def collget(self,data):
        if data is None:
            return
        self.list.append(data) 

    
    def outHtml(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.list:
            fout.write("<tr>")
            fout.write("<td>s%</td>" % data['url'])
            fout.write("<td>s%</td>" % data['title'].encode('utf-8'))
            fout.write("<td>s%</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")        
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    
    
    



