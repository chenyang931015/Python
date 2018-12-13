import urllib2
res = urllib2.urlopen('https://space.bilibili.com/39066904/video?tid=0&page=1&keyword=&order=pubdate')
ret = res.read()
print ret