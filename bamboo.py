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
    print("ũ�ѷ��� ����ϱ� ���ؼ��� ũ�� ����̹���� ũ�Ѹ��� �����ִ� ���α׷��� �ʿ��մϴ�. \n https://sites.google.com/a/chromium.org/chromedriver/downloads �� ������ �ü���� �´� ũ�� ����̹��� �ٿ�ް� �ٽ� �������ּ���\n �׸��� ũ�� ����̹��� �ּҸ� ����صμ���.")
    webLoc = input("�˻��� ���̽��� �볪���� �ּҸ� �Է����ּ���. ��ĭ �Է½ÿ��� ������б� �볪�������� �����մϴ�.\n ")
    if webLoc == "":
        webLoc = "http://snu.fbpage.kr/#/search"
    keyword = input("�˻�� �Է����ּ���\n")
    pageNum = int(input("ũ�Ѹ��� ������ ���� �Է����ּ���\n"))
    dirpath = input("Ű���� " + keyword  + " ������ ����� �����θ� �Է����ּ��� ��ĭ �Է½ÿ��� ����ȭ�鿡 ����˴ϴ�\n ")
    if(dirpath == "����"):
        dirpath = "/Users/yunsu/Google ����̺�/2018-summer/�۾����� ����/��������Ʈ/�볪����"
    elif dirpath == "":
        dirpath = os.path.expanduser("~/Desktop")
    chromeLoc = input("ũ�� ����̹��� ��ġ�� �����η� �Է����ּ���. ����� �������� chromedriver�� ������ �մϴ�.\n")
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
