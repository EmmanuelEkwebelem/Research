import requests
import pandas
import os
from bs4 import BeautifulSoup

cwd_original = os.getcwd()
output_files = cwd_original + '/data/2018/2018'

url_links = []
issue = 1
while issue != 13:
    url = f"https://link.springer.com/journal/256/volumes-and-issues/47-{issue}"
    issue = issue + 1
    url_links.append(url)
 
for link in range(len(url_links)):
    dates = ['-Jan','-Feb','-Mar','-Apr','-May','-Jun','-Jul','-Aug','-Sep','-Oct','-Nov','-Dec']
    page = requests.get(url_links[link])
    soup = BeautifulSoup(page.text, 'html.parser')
    Category = soup.find_all('li',class_='c-meta__item c-meta__item--block-sm-max')
    Categories = []
    for item in Category:
        C = item.text
        C = C.strip()
        C = C.replace('\n','')
        C = C.replace('Content type: ','')
        Categories.append(C)
    len(Categories)
    
    Title = soup.find_all('h3',class_='c-card__title')
    Titles = []
    for item in Title:
        T = item.text
        T = T.strip()   
        T = T.replace('\n','')
        Titles.append(T)
    len(Titles)
    Author = soup.find_all('div',class_='u-mb-8')
    Authors = []
    for item in Author:
        A = item.text
        A = A.strip()
        A = A.replace('\n',' ')
        Authors.append(A)
    len(Authors)
    A = [x for x in Categories if not x.startswith('Published')]
    B = [x for x in A if not x.startswith('Pages')]
    list0 = [x for x in B if not x.startswith('Open Access')]
    list1 = Titles 
    list2 = Authors
    df = pandas.DataFrame({'Article Class': pandas.Series(list0), 'Article Titles': pandas.Series(list1), 'List of Article Author Names': pandas.Series(list2)})

    
    df.to_csv(output_files + dates[link] + '.csv', index=False) 
    print('...finished with link: ' + url_links[link])

      
      
      
          
      
      
