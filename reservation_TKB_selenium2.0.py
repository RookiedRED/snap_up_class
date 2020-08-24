from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep  
import datetime

today = datetime.date.today()
x = datetime.timedelta(days = 6)
today = today + x

today = today.strftime('%Y-%m-%d')

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=options)

wait = WebDriverWait(browser, 10) # 等待載入10s

def login():
    browser.maximize_window()  # 最大化視窗

    browser.get('https://bookseat.tkblearning.com.tw/book-seat/student/login/toLogin')
    sleep(2)

    if alert_accept():
        print("alert showed")
    else :
        print("no alert")

    input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="id"]')))
    input.send_keys('your account')
    input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="pwd"]')))
    input.send_keys('your password')
    submit = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/form/div/div/div/table/tbody/tr[4]/td[2]/div[1]/a')))
    submit.click() # 點選登入按鈕
    
    sleep(3)

    ##確認彈出訊息視窗兩次
    if alert_accept():
        print("alert showed")
    else :
        print("no alert")
    
    if alert_accept():
        print("alert showed")
    else :
        print("no alert")


    #選擇課程
    slect_class = Select(browser.find_element_by_id("class_selector"))#找到選單
    slect_class.select_by_value("V5<6>KM:;<=>?A=BD@EGCI")#定位課程
    #選擇日期
    select_date = Select(browser.find_element_by_id("date_selector"))#找到選單
    select_date.select_by_value(today)#定位日期
    #選擇地區
    select_city = Select(browser.find_element_by_id("branch_selector"))#找到選單
    select_city.select_by_value("WA")#定位地區
    sleep(3)

    reserve_check = 0
    try:
        browser.find_element_by_css_selector('input[value="1"]').click()
        print("成功選取"+today+"第一場次")
    except:
        reserve_check += 1
        print("第一場次無法選取")

    try:
        browser.find_element_by_css_selector('input[value="2"]').click()
        print("成功選取"+today+"第二場次")
    except:
        reserve_check += 2
        print("第二場次無法選取")

    if reserve_check < 1:
        submit = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/section/article/table/tbody/tr[6]/td[2]/div[1]/a')))
        submit.click() # 點選送出按鈕
        print("預約 場次一、場次二 成功")
    elif reserve_check < 2:
        submit = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/section/article/table/tbody/tr[6]/td[2]/div[1]/a')))
        submit.click() # 點選送出按鈕
        print("預約 場次二 成功")
    elif reserve_check < 3:
        submit = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/section/article/table/tbody/tr[6]/td[2]/div[1]/a')))
        submit.click() # 點選送出按鈕
        print("預約 場次一 成功")
    else :
        print("預約失敗")
    sleep(3)

    if alert_accept():
        print("alert showed")
    else :
        print("no alert")

    if alert_accept():
        print("alert showed")
    else :
        print("no alert")   


def alert_accept():
    try:
        alert = browser.switch_to.alert
        print(alert.text)
        alert.accept()
        sleep(2)
        return alert    
    except:
        return False


if __name__=="__main__":

    login()
    