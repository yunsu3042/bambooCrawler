import selenium
import time
import bs4
import os
from selenium import webdriver
def writePage(driver, dirpath, keyword):
    headers = driver.find_elements_by_css_selector("small.text-muted.ng-binding")
    articles = driver.find_elements_by_css_selector("p.feedContent.ng-binding")
    assert len(headers) == len(articles)
    for i in range(len(articles)):
        header = headers[i]
        article = articles[i]
        writeFile(toSearch=keyword, header=header, article=article, dirpath=dirpath)
        
def writeFile(toSearch, header, article, dirpath):
    if toSearch == "":
        toSearch = "¿ ¿¿¿"
    path = dirpath + "/" + toSearch
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    column = article.text
    date = header.text.split("\n")[1]
    name = toSearch + "_" + date + ".txt"
    file = open(path + "/" + name, 'w')
    file.write(column)
    file.close()
    
def getPage(n):
    time.sleep(1)
    navi = driver.find_elements_by_xpath("//ul[@class='pagination pagination-sm']/li/a")
    if(n > 5):
        fastNextBtn = navi[len(navi) - 1]
        fastNextBtn.click()
        time.sleep(3)
        n = n - 5
        getPage(n)
    else:
        activeObj = driver.find_element_by_css_selector(".ng-scope.active")
        activePage = activeObj.find_element_by_css_selector(".ng-binding.ng-scope").text
        targetPage = int(activePage) + n - 1
        for idx in range(len(navi)):
            if(len(navi) == 7 and (idx == 0 or idx == 6)):
                continue
            if(len(navi) == 6 and (idx == 5)):
                continue
            page = navi[idx].find_element_by_css_selector(".ng-binding.ng-scope").text
            if int(page) == targetPage:
                targetPageBtn = navi[idx]
                targetPageBtn.click()
                break

    
def getNextPage(driver):
    activeObj = driver.find_element_by_css_selector(".ng-scope.active")
    curPage = activeObj.find_element_by_css_selector(".ng-binding.ng-scope").text
    curPage = int(curPage)
    navi = driver.find_elements_by_xpath("//ul[@class='pagination pagination-sm']/li/a")
    if curPage % 5 == 0:
        nextBtn = navi[len(navi) - 1]
        nextBtn.click()
        return True
    for idx in range(len(navi)):
        if(len(navi) == 7 and (idx == 0 or idx == 6)):
            continue
        if(len(navi) == 6 and (idx == 5)):
            continue
        page = navi[idx].find_element_by_css_selector(".ng-binding.ng-scope").text
        if int(page) == curPage + 1:
            nextBtn = navi[idx]
            nextBtn.click()
            return True
    return False

def getDriver(webLoc, chromeLoc):
    driver = webdriver.Chrome(chromeLoc)
    driver.implicitly_wait(3)
    driver.get(webLoc)
    return driver

def crawler(n, driver, dirpath, keyword):
    for i in range(n - 1):
        if(getNextPage(driver)):
            time.sleep(5)
            writePage(driver, dirpath, keyword)
            driver.implicitly_wait(5)
        else:
            print("¿¿ ¿¿ ¿¿ ¿¿¿ ¿¿¿¿.")
            break
        
def search():
    print("¿¿¿¿ ¿¿¿¿ ¿¿¿¿ ¿¿ ¿¿¿¿¿¿ ¿¿¿¿ ¿¿¿¿ ¿¿¿¿¿ ¿¿¿¿¿. \n https://sites.google.com/a/chromium.org/chromedriver/downloads ¿ ¿¿¿ ¿¿¿¿¿ ¿¿ ¿¿ ¿¿¿¿¿ ¿¿¿¿ ¿¿ ¿¿¿¿¿¿\n ¿¿¿ ¿¿ ¿¿¿¿¿ ¿¿¿ ¿¿¿¿¿¿.")
    webLoc = input("¿¿¿ ¿¿¿¿ ¿¿¿¿ ¿¿¿ ¿¿¿¿¿¿. ¿¿ ¿¿¿¿¿ ¿¿¿¿¿ ¿¿¿¿¿¿ ¿¿¿¿¿.\n ")
    if webLoc == "":
        webLoc = "http://snu.fbpage.kr/#/search"
    keyword = input("¿¿¿¿ ¿¿¿¿¿¿\n")
#     startPage = input("¿¿¿¿ ¿¿¿ ¿¿¿ ¿¿¿ ¿¿¿¿¿¿")
#     if startPage == "":
#         startPage = 0
#     else:
#         startPage = int(startPage)
    pageNum = int(input("¿¿¿¿ ¿¿¿ ¿¿ ¿¿¿¿¿¿\n"))
    dirpath = input("¿¿¿ '" + keyword  + "' ¿¿¿ ¿¿¿ ¿¿¿¿¿ ¿¿¿¿¿¿ ¿¿ ¿¿¿¿¿ ¿¿¿¿¿ ¿¿¿¿¿\n ")
    if(dirpath == "¿¿"):
        dirpath = "/Users/yunsu/Google ¿¿¿¿/2018-summer/¿¿¿¿ ¿¿/¿¿¿¿¿/¿¿¿¿"
    elif dirpath == "":
        dirpath = os.path.expanduser("~/Desktop")
    chromeLoc = input("¿¿ ¿¿¿¿¿ ¿¿¿ ¿¿¿¿¿ ¿¿¿¿¿¿. ¿¿¿ ¿¿¿¿ chromedriver¿ ¿¿¿ ¿¿¿.\n")
    if chromeLoc == "":
        chromeLoc = '/Users/yunsu/Downloads/chromedriver'

    driver = getDriver(webLoc, chromeLoc)
    lookup = driver.find_element_by_css_selector("input.form-control")
    lookup.clear()
    lookup.send_keys(keyword)
    search = driver.find_element_by_css_selector(".btn.btn-sm.btn-success")
    search.click()
    driver.implicitly_wait(5)
#     getPage(startPage)
    writePage(driver, dirpath, keyword)
    crawler(pageNum, driver, dirpath, keyword)
    driver.close()    


    
search()
    
    
