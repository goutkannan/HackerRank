from multiprocessing import Pool
import urllib.request

sites = [
    'https://www.yahoo.com/',
    'http://www.cnn.com',
    'http://www.python.org',
    'http://www.jython.org',
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
    'http://www.macrumors.com/',
    'http://arstechnica.com/',
    'http://www.reuters.com/',
    'http://abcnews.go.com/',
    'http://www.cnbc.com/',
    'http://www.cnbc.com/',
]


def job(url):
    print("Calling..", url)
    with urllib.request.urlopen(url) as u:
        return url, len(u.read())
    


if __name__== '__main__':
    p = Pool(processes=20)
    data = p.map(job, sites)
    p.close()
    print(data)
