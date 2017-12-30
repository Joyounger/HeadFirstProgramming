import urllib.request

page = urllib.request.urlopen("https://book.douban.com/subject/10561367/")
text = page.read().decode("utf-8")

print(text)