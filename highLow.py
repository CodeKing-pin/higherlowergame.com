from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
#List of all ques
r = requests.get('http://www.higherlowergame.com/questions/get/general')
data = r.json()
result = {}
for i in range(1560):
    key = data[i]['keyword']
    vol = data[i]['searchVolume']
    result[key] = vol
driver = webdriver.Chrome(options=options)
driver.get('http://www.higherlowergame.com/')

driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/span/section/div[2]/div/button[1]').click()

#Finding Correct answers


def action():
    f1 = driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/span/span/div/div[2]/div[1]/div[1]/div/div[1]/p[1]').text.split('”')[0].split('“')[1]
    f2 = driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/span/span/div/div[2]/div[1]/div[2]/div/div[1]/p[1]').text.split('”')[0].split('“')[1]
    r1 = int(result.get(f1))
    r2 = int(result.get(f2))
    if r1 > r2:  # lower
        driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/span/span/div/div[2]/div[2]/button[2]').click()
    else:
        driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/span/span/div/div[2]/div[2]/button[1]').click()


Score = input("Enter Your Score you want:- ")  # Enter your score
for i in range(int(Score)):
    action()
    WebDriverWait(driver, 50).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/span/span/div/div[2]/div[2]/button[1]')))
