#! /usr/bin/env python3

import glob
import html
import re

tuples = []
for file in glob.glob('websites/blogs.msdn.com/b/oldnewthing/archive/*/*/*/*.aspx'):
    markup = open(file).read()
    mat1 = re.search(r'<form name="aspnetForm" method="post" action="/b/oldnewthing/archive/(\d{4})/(\d{1,2})/(\d{1,2})/(\d+).aspx" id="aspnetForm">', markup)
    mat2 = re.search(r'<title>\s*(.*?)\s*- The Old New Thing', markup)
    if mat1 and mat2:
        y = int(mat1.group(1))
        m = int(mat1.group(2))
        d = int(mat1.group(3))
        iso_date = "{:d}-{:02d}-{:02d}".format(y,m,d)
        post_id = int(mat1.group(4))
        title = html.unescape(mat2.group(1))
        tuples.append((iso_date, post_id, title))
tuples.sort()
for (iso_date, post_id, title) in tuples:
    print("{}|{}|{}".format(iso_date, post_id, title))
