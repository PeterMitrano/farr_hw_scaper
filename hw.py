import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.math.wpi.edu/Course_Materials/MA2071C16/Hw/hw2.html')
soup = BeautifulSoup(page.text,'html.parser')
lines = soup.find('pre').text.split('\n')

for lin_num in range(3,len(lines)-1):
    section = lines[lin_num].split(" ")[0]
    problems = lines[lin_num].split(" ")[27].split(',')
    print section, ":  ", ' '.join([p.encode('ascii', 'ignore') for p in problems])


