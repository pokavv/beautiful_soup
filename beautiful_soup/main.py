# Beautiful_soup doc : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import lxml

with open('beautiful_soup/website.html', 'rt', encoding='UTF8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')

all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get('href'))
    print()

heading = soup.find(name='h1', id='name')
print(heading.getText())

section_heading = soup.find(name='h3', class_='heading')
print(section_heading.getText())

name = soup.select_one(selector='#name')
print(name)

headings = soup.select('.heading')
print(headings)