import requests
from bs4 import BeautifulSoup
import pprint
import numpy as np

#Loop to go over all pages
p = range(1, 9, 1)


for pa in p:
    response = requests.get('https://news.ycombinator.com/news?p='+str(pa))
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find(id='score_32767287'))
#selectors
# .class , # pt id
# s = soup.select('.score')
# print(s)

    links = soup.select('.titlelink')

    print(links)

    subtext = soup.select('.subtext')

    def sort_by_votes(hnlist):
        return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

    def create_custom_hn(links, subtext):
        hn = []
        for idx, item in enumerate(links):
            title = links[idx].getText()
            href = links[idx].get('href', None)
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title,
                    'link': href,
                    'votes': points})
        return sort_by_votes(hn)

#print(create_custom_hn(links, votes))
    pprint.pprint(create_custom_hn(links,subtext))