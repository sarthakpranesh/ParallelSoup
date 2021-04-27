from parallelsoup import ParallelSoup
from datetime import datetime
import time

urls = []
for i in range(0, 10):
    urls.append("https://www.imdb.com/search/title/?countries=in&adult=include&start=" + str(50*i + 1) + "&ref_=adv_nxt")

def extractor(soup):
    data = []
    for item in soup.findAll('div', attrs={'class':'lister-item mode-advanced'}):
        title = item.find('div', attrs={'class':'lister-item-content'}).h3.a
        if title != None:
            data.append(title.text)
    return data

# Serial Execution
from bs4 import BeautifulSoup
import requests
serialTimeStart = time.time()
data = []
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")
    data = data + extractor(soup)
serialTimeStop = time.time()


# ParallelSoup
parallelTimeStart = time.time()
ps = ParallelSoup(8, urls, extractor)
ps.start()
dataParallel = ps.get()
parallelTimeStop = time.time()

print('Serial Execution Time(seconds):', serialTimeStop - serialTimeStart)
print('ParallelSoup Execution Time(seconds):', parallelTimeStop - parallelTimeStart)

print('Checking the Parallel Soup Result with Serial Result')
resultsNotEqual = False
for i in range(0, len(data)):
    if data[i] not in dataParallel:
        print('Index at fault:', i, '\t Val:', data[i])
        resultsNotEqual = True
        break
print('Are both Serial and ParallelSoup scraping results equal?', not resultsNotEqual)
