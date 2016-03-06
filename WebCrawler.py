import urllib2
import time
from bs4 import BeautifulSoup

urlString1 = 'http://www.indeed.com/jobs?q='
urlString2 = '&l='
addJStoQuery = '+javascript'
titleQueryList = ['react', 'angular', 'node', 'jQuery', 'mongo', 'npm', 'git']
resultsList = []

def findNumJobListings():
    for titleQuery in titleQueryList:
        page = urllib2.urlopen(urlString1 + titleQuery + addJStoQuery + urlString2).read()
        soup = BeautifulSoup(page, "html.parser")
        result = str(soup.find(id='searchCount').get_text())
        splitResult = result.split()
        resultsList.append(titleQuery + ': ' + splitResult[len(splitResult)-1])
        # Delay for five seconds between requests to the server, just to be polite
        time.sleep(5)
        
findNumJobListings()
print(resultsList)