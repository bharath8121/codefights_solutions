from HTMLParser import HTMLParser
def pageComplexity(document):
    parser = MyHTMLParser()
    parser.feed(document)
    result = parser.getResult()
    return result[max(result.keys())]
    
    
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.current = ''
        self.result = dict()
        self.count = 0
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        self.current = tag
        self.count+=1

    def handle_endtag(self, tag):
        if self.current == tag:
            if self.count in self.result.keys() and tag not in self.result[self.count]:
                self.result[self.count].append(tag)
            else:
                self.result.update({self.count:[tag]})
            self.current = ''
        self.count -= 1

    def handle_data(self, data):
        pass
    
    def getResult(self):
        return self.result
