import json
  
# Opening JSON file
f = open('test.json')
data = json.load(f)
f.close()

from parallelsoup import ParallelSoup

urls = []
for i in range(0, 100):
    urls.append("https://www.imdb.com/search/title/?countries=in&adult=include&start=" + str(50*i + 1) + "&ref_=adv_nxt")

def extractor(soup):
    data = []
    for item in soup.findAll('div', attrs={'class':'lister-item mode-advanced'}):
        title = item.find('div', attrs={'class':'lister-item-content'}).h3.a
        if title != None:
            data.append(title.text)
    return data

ps = ParallelSoup(8, urls, extractor)
ps.start()

file = open('read.txt', 'w')
file.write(",".join(ps.get()))
file.close()
