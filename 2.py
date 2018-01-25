import re, urllib.request

page = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()

#''.join(re.findall('[a-z]', page))
