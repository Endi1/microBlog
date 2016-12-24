# microBlog
## Blog using Flask and markdown!

microBlog automatically compiles your markdown files stored in `/pages`. Run `python app.py` and visit `localhost:5000`
to view the contents of your website.

### Installation
You will need pip to use microBlog. Run `git clone https://github.com/endi1/microblog` to clone the latest version of 
microBlog. After that run `cd microblog && pip install -r requirements.txt` to install all needed dependencies.

### Viewing your website
To view the contents of your website, simply run `python app.py` and visit `http://localhost:5000`.

### Markdown pages
Pages are stored on the `/pages` directory and have a `.md` extension. You will notice that the existing examples have 
some meta-data on the top of the file. 

```
title: Blog
url: /blog
```

You will also notice that `index.md` only has `title`, `url` is not necessary for the `index.md` file although the 
`index.md` file itself is necessary as it is the homepage for your website. Missing from both examples is the `layout` 
variable, if it's missing then the page uses `/templates/default.html` by default, if you want to use a different layout
for a particular page, simply add this variable. For example, `layout: post` will use `/templates/post.html` as a 
layout. Layouts use Jinja for markup. 

### Variables
There are some variables available for you to use in your layouts. Most of these have information about the page you 
are currently on. Some of these variables are:

TBA
