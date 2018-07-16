import selenium
import time
import bs4
import os
from selenium import webdriver

def writePage(driver, dirpath):
    headers = driver.find_elements_by_css_selector("small.text-muted.ng-binding")
    articles = driver.find_elements_by_css_selector("p.feedContent.ng-binding")
    assert len(headers) == len(articles)
    for i in range(len(articles)):
        header = headers[i]
        article = articles[i]
        writeFile(toSearch=toSearch, header=header, article=article, dirpath=dirpath)
        
def writeFile(toSearch, header, article, dirpath):
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
    
def getNextPage(driver):
    activeObj = driver.find_element_by_css_selector(".ng-scope.active")
    curPage = activeObj.find_element_by_css_selector(".ng-binding.ng-scope").text
    curPage = int(curPage)
    navi = driver.find_elements_by_xpath("//ul[@class='pagination pagination-sm']/li/a")
    if curPage % 5 == 0:
        nextBtn = navi[len(navi) - 1]
    for idx in range(len(navi)):
        if(len(navi) == 7 and (idx == 0 or idx == 6)):
            continue
        if(len(navi) == 6 and (idx == 5)):
            continue
        page = navi[idx].find_element_by_css_selector(".ng-binding.ng-scope").text
        if int(page) == curPage + 1:
            nextBtn = navi[idx]
    nextBtn.click()

def getDriver(webLoc, chromeLoc):
    driver = webdriver.Chrome(chromeLoc)
    driver.implicitly_wait(3)
    driver.get(webLoc)
    return driver

def crawler(n, driver, dirpath):
    for i in range(n - 1):
        getNextPage(driver)
        time.sleep(3)
        writePage(driver, dirpath)
        driver.implicitly_wait(3)
        
def search():
    print("크롤러를 사용하기 위해서는 크롬 드라이버라는 크롤링을 도와주는 프로그램이 필요합니다. \n https://sites.google.com/a/chromium.org/chromedriver/downloads 에 접속해 운영체제에 맞는 크롬 드라이버를 다운받고 다시 실행해주세요\n 그리고 크롬 드라이버의 주소를 기억해두세요.")
    webLoc = input("검색할 페이스북 대나무숲 주소를 입력해주세요. 빈칸 입력시에는 서울대학교 대나무숲으로 접속합니다.\n ")
    if webLoc == "":
        webLoc = "http://snu.fbpage.kr/#/search"
    keyword = input("검색어를 입력해주세요\n")
    pageNum = int(input("크롤링할 페이지 수를 입력해주세요\n"))
    dirpath = input("키워드 " + keyword  + " 폴더가 저장될 절대경로를 입력해주세요 빈칸 입력시에는 바탕화면에 저장됩니다\n ")
    if(dirpath == "윤수"):
        dirpath = "/Users/yunsu/Google 드라이브/2018-summer/글쓰기의 기초/팀프로젝트/대나무숲"
    elif dirpath == "":
        dirpath = os.path.expanduser("~/Desktop")
    chromeLoc = input("크롬 드라이버의 위치를 절대경로로 입력해주세요. 경로의 마지막은 chromedriver로 끝나야 합니다.\n")
    if chromeLoc == "":
        chromeLoc = '/Users/yunsu/Downloads/chromedriver'
    driver = getDriver(webLoc, chromeLoc)
    lookup = driver.find_element_by_css_selector("input.form-control")
    lookup.clear()
    lookup.send_keys(keyword)
    search = driver.find_element_by_css_selector(".btn.btn-sm.btn-success")
    search.click()
    driver.implicitly_wait(5)
    writePage(driver, dirpath)
    crawler(pageNum, driver, dirpath)
    driver.close()

search()
