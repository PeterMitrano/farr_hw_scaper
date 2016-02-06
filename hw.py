#! /usr/bin/python

import requests
from bs4 import BeautifulSoup

pages = requests.get('http://www.math.wpi.edu/Course_Materials/MA2071C16/Hw/hwk.html')

soup = BeautifulSoup(pages.text,'html.parser')
current_hw_num = len(soup.findAll('a'))-1
print current_hw_num
page = requests.get('http://www.math.wpi.edu/Course_Materials/MA2071C16/Hw/hw'+str(current_hw_num)+'.html')
soup = BeautifulSoup(page.text,'html.parser')
lines = soup.find('pre').text.split('\n')

for lin_num in range(3,len(lines)-1):
    section = lines[lin_num].split(" ")[0]
    last = len(lines[lin_num].split(" "))-1
    problems = lines[lin_num].split(" ")[last].split(',')
    print section, ":  ", ' '.join([p.encode('ascii', 'ignore') for p in problems])


