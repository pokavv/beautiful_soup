# Beautiful_soup doc : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import lxml

with open('website.html', 'rt', encoding='UTF8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')

