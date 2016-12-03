import os
from flask import Flask, redirect, render_template

from Page import Page


app = Flask(__name__)


def getPages(folder_name):
    filenames = os.listdir('pages')
    pages = []
    pages = [Page('pages/'+filename) for filename in filenames]
    return pages

def findPageToPrint(page_url):
    all_pages = getPages('pages')
    page_to_print = None
    print(page_url)

    for page in all_pages:
        if page.filename != 'pages/index.md':
            if page.meta['url'][0] == page_url:
                page_to_print = page

    return page_to_print

def renderPage(page):
    meta = page.getMeta()
    content = page.getHTML()
    pages = getPages('pages')

    return render_template(meta['layout'], meta=meta, content=content, pages=pages)


@app.route('/', defaults={'first_level': '', 'second_level': ''})
@app.route('/<first_level>', defaults={'second_level': ''})
@app.route('/<first_level>/<second_level>')
def index(first_level, second_level):
    page_url = '/' + first_level + '/' + second_level if second_level != '' else '/' + first_level

    if page_url == '/':
        page_to_print = Page('pages/index.md')
    else:
        page_to_print = findPageToPrint(page_url)
        if page_to_print == None:
            return redirect('/')
    return renderPage(page_to_print)
        

if __name__ == '__main__':
    app.run(debug=True)
