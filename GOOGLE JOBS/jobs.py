import pandas
from bs4 import BeautifulSoup
import html5lib
import requests
import csv  
from datetime import datetime 



def get_url (position,location, page):
    TEMPLATES = "https://www.monster.com/jobs/search?q={}&where={}&page={}&so=m.h.s"
    url = TEMPLATES.format(position,location,page)
    return url
a = input("ENTER NNUMBER OF PAGES : ")
b = input("ENTETR JOB LOCATION : ")
c = input("ENTER NAME OF JOB : ")
url = get_url(a,b,c)

response =requests.get(url)
# print(response)
# print(response.reason)
soup = BeautifulSoup(response.text ,"html5lib")
# print(soup.prettify())
link_list = []
job_link = soup.find_all("a")
clue = "https://www.monster.com/job-openings/"
for links in job_link:
    z = links.get('href')
    if z and clue in z:
        link_list.append(z)

print(link_list)
print(len(link_list))

for urls in link_list:
    my_urls = requests.get(urls).text 
    soup_urls = BeautifulSoup(my_urls,"html5lib")

    # Find all divs with class "article-body-text"
    boxes = soup_urls.find_all("div", class_="descriptionstyles__DescriptionContainerOuter-sc-7dvtrp-0 iJISVC")
    # body_written = False  # Flag to track if "BODY" has been written
    for box in boxes:
        paragraphs = box.find_all('p')
        for paragraph in paragraphs:
            you = paragraph.get_text(strip=True)
        print(you )    


