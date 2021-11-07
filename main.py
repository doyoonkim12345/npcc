import datetime
import re
import csvwriter
import requests
from selenium import webdriver


from bs4 import BeautifulSoup

def crawler(tag, Class):
    #print(response.content)
    soup = BeautifulSoup(response, 'html.parser')
    return soup.find_all(tag, class_= Class)

def tagRemover(tagtext):
    tagtext = re.sub('<.+?>', '', str(tagtext), 0).strip()
    return tagtext[1:len(tagtext) - 1]

browser = webdriver.Chrome()
browser.get("https://www1.president.go.kr/petitions")

response = browser.page_source
#response = requests.get('https://www1.president.go.kr/petitions')

notices = crawler('a', 'cb')
contentnum = 0
startlink = 'https://www1.president.go.kr/petitions/'
endlink = '?navigation=petitions'

print(notices)

for n in notices:
    temp = n.get('href')
    print(temp)
    if temp[0] == 'h' and not 'best' in temp:
        contentnum = int(temp[39:45])
        print(contentnum)
        break

now = datetime.datetime.now()
print(now)
print(contentnum)

for num in range(contentnum, 0, -1):
    link = startlink + str(num) + endlink
    response = requests.get(link)
    try:
        print(link)
        title = tagRemover(crawler('h3', 'petitionsView_title'))
        print(title)
        info = crawler('ul', 'petitionsView_info_list')
        print('start')
        infolist = tagRemover(info).split('\n')
        category = str(infolist[1][4:])
        print(category)
        startdate = infolist[2][4:]
        print(startdate)
        enddate = infolist[3][4:]
        print(enddate)
        addressor = infolist[4][3:]
        print(addressor)
        convertdate = datetime.datetime.strptime(enddate, "%Y-%m-%d")
        content = str(tagRemover(crawler('div', 'View_write')).replace('											','')).replace("\r", " ").replace('\n', '').replace('&gt;',">")
        print(content)
        if convertdate < now:
            break
        csvwriter.csvWrite(title, category, startdate, enddate, content, addressor)
    except IndexError:
        pass
    print('end')
