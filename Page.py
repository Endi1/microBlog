import markdown

class Page:
    def __init__(self, filename):
        md = markdown.Markdown(extensions = ['markdown.extensions.meta'])
        self.filename = filename

        with open(filename, 'r') as mdfile:
            self.html = md.convert(mdfile.read())

        self.meta = md.Meta

    def __checkKeyExistence(self, key):
        return self.meta[key][0] if key in self.meta else None

    def getMeta(self):
        meta = {
            'title': self.__checkKeyExistence('title'),
            'layout': self.meta['layout'][0] if 'layout' in self.meta else 'default.html',
            'url': self.__checkKeyExistence('url')
        }

        return meta

    
    def getHTML(self):
        return self.html
