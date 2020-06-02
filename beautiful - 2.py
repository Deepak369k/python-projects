import requests
from bs4 import BeautifulSoup
import clipboard

quote_author = []
i = 1
while i < 5:
    base_url = 'https://www.brainyquote.com'
    print('Enter Brainy Quote Page URL: ')
    url = input()
    if url == '':
        url = clipboard.paste()

    r = requests.get(url)
    #print(r.status_code)

    page = BeautifulSoup(r.content, 'html.parser')
    #print(page.prettify())


    containers = page.find_all('div', class_= 'clearfix')
    #print(len(containers))

    #container = containers[0]

    #print(container)

    for container in containers:
        quote0 = container.find('a', {'title':'view quote'}).text
        print(quote0)

        author0 = container.find('a', {'title':'view author'}).text
        print(author0)


    next_ul = page.find_all('ul', class_='pagination bq_pageNumbers pagination-centered pagination-sm')
    #print(next_ul)
    ul = next_ul[0]
    for li in ul.findAll('li'):
        if "Next" in li.text:
            link = li.findAll('a')
            #print(link)
            next_page_url = link[0]['href']
            next_page_url = url + next_page_url
           # print(url)

    i += 1
    print('#############################')
























