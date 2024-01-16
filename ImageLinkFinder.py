import pandas as pd
import urllib3


def linksFromMainPage(url):
    src = http.request('GET', url).data.decode("utf-8").split()
    links = []
    for ind, token in enumerate(src):
        if 'href="/coinfacts' in token and 'MS' in src[ind + 2]:
            links.append('https://pcgs.com' + token.split('"')[1])
    return links


def imgLinksFromLinkList(linkList):
    imgPageLinks = []
    for index, link in enumerate(linkList):
        src = http.request('GET', link).data.decode("utf-8").split()
        for i in src:
            if 'href="/coinfacts/' in i and 'View' in i:
                imgPageLinks.append('https://pcgs.com' + i[6:-6])
    return imgPageLinks


def onePageScrape(url):
    code = urllib3.request('GET', url).data.decode("utf-8").split()
    links = []
    grades = []
    for index2, token in enumerate(code):
        if 'href="https://images' in token:
            links.append(token[6:-1])
            for i in range(4, 7):
                if '</p>' in code[index2 + i]:
                    grade = code[index2 + i][:2]
            if '<' in grade:
                grade = grade[:1]
            grades.append(grade)
    return links, grades


def mainLinkScrape(link, coinType):
    print('    - Scraping smaller page links')
    smallerLinks = linksFromMainPage(link)
    print('    - Finding image page links')
    smallerImgLinks = imgLinksFromLinkList(smallerLinks)
    print('    - Extracting images from image page links (this takes the longest)')
    typeGrades = []
    typeLinks = []
    for index, searchLink in enumerate(smallerImgLinks):
        results = onePageScrape(searchLink)
        for j in results[0]:
            typeLinks.append(j)
        for j in results[1]:
            typeGrades.append(j)
    typeList = [coinType for obj in typeLinks]
    return typeLinks, typeGrades, typeList


with open('CoinTypeLinks.txt') as f:
    mainLinks = f.readlines()
with open('CoinTypes.txt') as f:
    coinTypes = f.readlines()
for ind in range(len(mainLinks)):
    mainLinks[ind] = mainLinks[ind][:-1]
    coinTypes[ind] = coinTypes[ind][:-1]

allLinks = []
allTypes = []
allGrades = []
http = urllib3.PoolManager(retries=False)
for ind, link in enumerate(mainLinks):
    print('Searching for', coinTypes[ind], 'images')
    result = mainLinkScrape(link, coinTypes[ind])
    for i in result[0]:
        allLinks.append(i)
    for i in result[1]:
        allGrades.append(i)
    for i in result[2]:
        allTypes.append(i)

dataDict = {'Image Link': allLinks, 'Coin Type': allTypes, 'Grade': allGrades}
data = pd.DataFrame.from_dict(dataDict)
print(data)
with open('secondAttemptImageLinks.csv', 'w') as file:
    data.to_csv(file)
