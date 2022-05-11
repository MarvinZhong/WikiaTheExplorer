import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pyautogui
import time

PATH = Service('webdrivers/msedgedriver.exe')
driver = webdriver.Edge(service=PATH)


def getLink(para):
    paragraph = '//*[@id="mw-content-text"]/div[1]/p['+str(para)+']'
    paragraph = driver.find_element(by=By.XPATH, value=paragraph)
    firstParagraphText = paragraph.text
    i = 1
    while firstParagraphText == "":
        # linking = '//*[@id="mw-content-text"]/div[1]/p[2]/a[1]'
        # linking = driver.find_element(by=By.XPATH, value=linking)
        i += 1
        getLink(i)
        if i == 10:
            break
    linking = '//*[@id="mw-content-text"]/div[1]/p[' + str(i) + ']/a[1]'
    linking = driver.find_element(by=By.XPATH, value=linking)
    print(paragraph, linking)
    return linking


# //*[@id="mw-content-text"]/div[1]/p[2]/a[1]
# //*[@id="mw-content-text"]/div[1]/p[2]/a
# //*[@id="mw-content-text"]/div[1]/p[1]/a[1]
# //*[@id="mw-content-text"]/div[1]/p[2]/span/a
# //*[@id="mw-content-text"]/div[1]/p[2]/a[1]
# //*[@id="mw-content-text"]/div[1]/p[2]/a[1]
# //*[@id="mw-content-text"]/div[1]/p[3]/a[1]
# //*[@id="mw-content-text"]/div[1]/p[2]/a[1]
# //*[@id="mw-content-text"]/div[1]/p/a[1]
# //*[@id="mw-content-text"]/div[1]/p[1]/a[1]
# //*[@id="mw-content-text"]/div[1]/p[2]/a[2]
exploring = True
# while True:
# while in range 2
wayPath = []
driver.get('http://en.wikipedia.org/wiki/Special:Random')
# for _ in range(3):
while exploring:

    # wait for page ready
    time.sleep(1)
    # firstParagraph = '//*[@id="mw-content-text"]/div[1]/p[1]'
    para = 0
    # paragraph = '//*[@id="mw-content-text"]/div[1]/p[' + str(para) + ']'
    paragraph = '//*[@id="mw-content-text"]/div[1]/p'

    # get title of current page
    title = driver.title
    # split title by - and get the first part
    title = title.split(' - ')[0]
    # if title start by 'List of ' remove it
    if title.startswith('List of '):
        title = title[9:]
    # remove last ' ' from title
    # title = title.strip()
    # if title is 'Philosophy' then break
    if title == 'Philosophy':
        # append to wayPath
        wayPath.append(title)
        exploring = False
    # getting the first paragraph
    # firstLink = getLink(p)
    paragraph = driver.find_element(by=By.XPATH, value=paragraph)
    firstParagraphText = paragraph.text
    # split firstParagraphText by ' ' to list
    firstParagraphText = firstParagraphText.split(' ')
    # all words in firstParagraphText lowercase
    firstParagraphText = [word.lower() for word in firstParagraphText]
    # delete all words in range startby '(' end by ')'
    for i in range(len(firstParagraphText)):
        if firstParagraphText[i].startswith('('):
            while True:
                firstParagraphText[i] = ''
                i += 1
                if firstParagraphText[i].endswith(')'):
                    break
        break
    # first title is the first word title
    firstTitle = title.split(' ')[0]
    # lowercase first title
    firstTitle = firstTitle.lower()
    while firstTitle not in firstParagraphText:
        # linking = '//*[@id="mw-content-text"]/div[1]/p[2]/a[1]'
        # linking = driver.find_element(by=By.XPATH, value=linking)
        para += 1
        paragraph = '//*[@id="mw-content-text"]/div[1]/p[' + str(para) + ']'
        rawParagraph = driver.find_element(by=By.XPATH, value=paragraph)
        firstParagraphText = rawParagraph.text
        firstParagraphText = firstParagraphText.split(' ')
        firstParagraphText = [word.lower() for word in firstParagraphText]
        for i in range(len(firstParagraphText)):
            if firstParagraphText[i].startswith('('):
                while True:
                    firstParagraphText[i] = ''
                    i += 1
                    if firstParagraphText[i].endswith(')'):
                        break
            break
        # getLink(i)
        # if i == 10:
        #     break
    # paragraph + '/a[1]'
    # if this ')' found then break
    # if ')' in firstParagraphText:

    # if para == 0:
    #     linking = '//*[@id="mw-content-text"]/div[1]/p/a[1]'
    # # elif
    # else:
    #     linking = '//*[@id="mw-content-text"]/div[1]/p[' + str(para) + ']/a[1]'
    # get link text
    linking = paragraph + '/a[1]'
    # linking = paragraph + '/a[1]'
    firstLink = driver.find_element(by=By.XPATH, value=linking)
    linkText = firstLink.get_attribute('name')
    # try not get link in ( )
    # linkText = firstLink.get_attribute('name')
    # index = 1
    # while linkText not in firstParagraphText:
    #     if para == 0:
    #         break
    #     index += 1
    #     linking = '//*[@id="mw-content-text"]/div[1]/p[' + str(para) + ']/a[' + str(index) + ']'
    #     firstLink = driver.find_element(by=By.XPATH, value=linking)
    #     linkText = firstLink.get_attribute('name')
    # getting the first link's link
    link = firstLink.get_attribute('href')
    # if firstLink == ' ':
    #     continue
    # split link by / and get last word
    link = link.split('/')[-1]
    # if link have a '_' replace with ' '
    link = link.replace('_', ' ')
    # print(title, link)
    # wayPath = os.path.join(title, link)
    # append in wayPath if
    if title in wayPath:
        exploring = False
    else:
        # append title to wayPath
        wayPath.append(title)
    print(para)
    print(wayPath)
    # click firstLink
    # save wayPath to csv file
    # get link's title
    # get link's link
    # append link's title and link's link to csv file

    firstLink.click()
    # wayPath list split by \
    # wayPath = wayPath.split('\\')
    # if title is in wayPath list continue
    # if
    # break
